# astro-gearbox: Exoplanet Magnetic Habitability Triage

`astro-gearbox` is a lightweight Python package designed to calculate the **Gearbox Stress Index** ($G_s$) for exoplanetary datasets. 

Current habitability assessments often suffer from a thermal bias, prioritizing the circumstellar habitable zone while neglecting Star-Planet Magnetic Interactions (SPMI). High stellar magnetic torque, particularly from fully convective M-Dwarf hosts, can drive catastrophic magnetohydrodynamic (MHD) atmospheric stripping.

This tool provides a computationally efficient, continuous scalar metric to quantify a planet's magnetic coupling to its host star, allowing researchers to quickly filter large databases (like the NASA Exoplanet Archive) to identify **Magnetic Sanctuaries**—targets optimized for JWST transmission spectroscopy and high-fidelity 3D MHD modeling.

## Methodology: The $G_s$ Equation
The Gearbox Stress Index quantifies the relative magnetic coupling between an exoplanet and its host star. It is derived from the geometric ratio of the planetary radius (the "antenna") to its orbital distance (the "shield"), heavily penalized by the convective magnetic activity of the host star. 

The index is calculated as:

$$G_s = \left( \frac{R_p}{a} \right)^3 \times \left( \frac{1}{M_*} \right)^3$$

**Where:**
* **$R_p$ (Planetary Radius):** Measured in Jupiter Radii. Larger cross-sections capture more stellar wind plasma.
* **$a$ (Semi-major Axis):** Measured in AU. Magnetic pressure drops via the inverse-cube law.
* **$M_*$ (Stellar Mass):** Measured in Solar Masses. Represents the "Stellar Penalty." Because magnetic dynamo efficiency in the convective envelope scales inversely with stellar mass, lower-mass stars (M-Dwarfs) inflict an exponentially higher magnetic torque penalty on close-in planets.

**Interpretation:**
* **$G_s < 0.1$ (Magnetic Sanctuary):** Low stellar torque; optimal candidates for long-term atmospheric retention and JWST follow-up (e.g., Kepler-452 b, Kepler-62 f).
* **$G_s > 1.0$ (High Stress):** Magnetohydrodynamically compromised; severe risk of atmospheric stripping and inductive heating regardless of thermal equilibrium (e.g., TRAPPIST-1 e).

## Installation
*(Coming soon to PyPI)*
`pip install astro-gearbox`

## Quick Start
```python
from gearbox import GearboxAnalyzer

# Load NASA Exoplanet Archive CSV
analyzer = GearboxAnalyzer("exoplanet_data.csv")

# Identify rocky planets in the warm zone with low magnetic stress
sanctuaries = analyzer.get_sanctuaries()
print(sanctuaries[['pl_name', 'pl_orbsmax', 'st_mass', 'Gs_Score']])