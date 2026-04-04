import pandas as pd
import numpy as np

# 1. Load the NASA Archive
try:
    df = pd.read_csv("exoplanet_data.csv", comment='#')
    print(f"Successfully loaded {len(df)} planets.")

    # 2. Clean and Calculate Gs Score
    # We drop rows missing our core 'gears'
    df_clean = df.dropna(subset=['pl_name', 'pl_orbsmax', 'pl_radj', 'st_mass']).copy()
    
    # Formula: Gs = (Rp/a)^3 * (1/Ms)^3
    df_clean['Gs_Score'] = ((df_clean['pl_radj'] / df_clean['pl_orbsmax'])**3) * ((1 / df_clean['st_mass'])**3)

    # 3. ANALYSIS A: General Magnetic Sanctuaries (Any planet Gs < 0.1)
    gen_sanctuaries = df_clean[df_clean['Gs_Score'] < 0.1]
    top_10_gen = gen_sanctuaries.sort_values('Gs_Score').head(10)

    # 4. ANALYSIS B: "Warm Zone" Sanctuaries (The Thesis Focus)
    # Filter for Rocky Planets (Radius < 2.0 Earth Radii, which is ~0.18 Jupiter Radii)
    # And Inner Systems (Distance < 5.0 AU)
    df_warm = df_clean[(df_clean['pl_radj'] < 0.18) & (df_clean['pl_orbsmax'] < 5.0)].copy()
    warm_sanctuaries = df_warm[df_warm['Gs_Score'] < 0.1]
    top_10_warm = warm_sanctuaries.sort_values('Gs_Score').head(10)

    # 5. PRINT RESULTS
    print("\n" + "="*50)
    print("TABLE 1: GENERAL MAGNETIC SANCTUARIES (ALL PLANETS)")
    print("="*50)
    print(top_10_gen[['pl_name', 'st_mass', 'pl_orbsmax', 'pl_radj', 'Gs_Score']])

    print("\n" + "="*50)
    print("TABLE 2: WARM ZONE SANCTUARIES (ROCKY/INNER SYSTEM)")
    print("="*50)
    if not top_10_warm.empty:
        print(top_10_warm[['pl_name', 'st_mass', 'pl_orbsmax', 'pl_radj', 'Gs_Score']])
    else:
        print("No rocky planets in this dataset met the Gs < 0.1 threshold.")

except Exception as e:
    print(f"Error during triage: {e}")