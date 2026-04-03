from gearbox import GearboxAnalyzer

# 1. Initialize the analyzer with the NASA data
print("Initializing Gearbox Stress Index (Gs) analysis...")
analyzer = GearboxAnalyzer("exoplanet_data.csv")

# 2. Extract the Warm Zone Sanctuaries
sanctuaries = analyzer.get_sanctuaries(max_gs=0.1, min_au=0.7, max_au=1.5)

# 3. Print Table 2
print("\n--- TABLE 2: HIGH-PRIORITY JWST MAGNETIC SANCTUARIES ---")
print(sanctuaries[['pl_name', 'pl_orbsmax', 'st_mass', 'Gs_Score']].head(10).to_string(index=False))