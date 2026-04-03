import pandas as pd
import numpy as np

class GearboxAnalyzer:
    """
    A tool to calculate the Gearbox Stress Index (Gs) for exoplanets.
    Identifies Magnetic Sanctuaries vs. Magnetohydrodynamically compromised worlds.
    """
    def __init__(self, data_path):
        self.df = self.df = pd.read_csv(data_path, comment='#')
        self.earth_radius_jup = 1 / 11.2

    def calculate_gs_index(self):
        """Applies the continuous Gs metric to the dataset."""
        # Filter out incomplete data
        valid_data = self.df[(self.df['pl_radj'] > 0) & 
                             (self.df['pl_orbsmax'] > 0) & 
                             (self.df['st_mass'] > 0)].copy()

        # 1. Raw Geometric Coupling (R_p / a)^3
        valid_data['Gs_Raw'] = (valid_data['pl_radj']**3) / (valid_data['pl_orbsmax']**3)
        
        # 2. Stellar Magnetic Penalty (1 / M_*)^3
        valid_data['Sp_Penalty'] = (1.0 / valid_data['st_mass'])**3
        
        # 3. Final Gs Score
        valid_data['Gs_Score'] = valid_data['Gs_Raw'] * valid_data['Sp_Penalty']
        
        self.df = valid_data
        return self.df

    def get_sanctuaries(self, max_gs=0.1, min_au=0.7, max_au=1.5, max_radius_earth=1.6):
        """Filters for rocky planets in the thermal habitable zone with low magnetic stress."""
        if 'Gs_Score' not in self.df.columns:
            self.calculate_gs_index()
            
        max_rad_jup = max_radius_earth * self.earth_radius_jup
        
        sanctuaries = self.df[
            (self.df['pl_radj'] <= max_rad_jup) &
            (self.df['pl_orbsmax'] >= min_au) &
            (self.df['pl_orbsmax'] <= max_au) &
            (self.df['Gs_Score'] <= max_gs)
        ].copy()
        
        return sanctuaries.sort_values(by='Gs_Score', ascending=True)