# Predicting Mechanical Properties of Cu-Ni Alloys Using Molecular Dynamics and Machine Learning

## Overview
This project investigates how composition, temperature, and strain rate affect the mechanical behavior of Cu-Ni alloys. LAMMPS molecular dynamics simulations were used to generate stress-strain data, which was then used to train a machine learning model to predict key material properties.

---

## Methodology

### 1. Molecular Dynamics Simulation (LAMMPS)
- Built FCC lattice models with varying nickel content: 0%, 25%, and 50% Ni
- Used the EAM interatomic potential (`CuNi.eam.alloy`) to model atomic interactions
- Equilibrated systems using the NPT ensemble with assigned initial velocities
- Applied uniaxial tensile deformation along the z-axis
- Ran 12 simulations across the following parameter space:
  - **Temperatures:** 300K, 500K
  - **Strain Rates:** 0.001, 0.0005
  - **Compositions:** 0%, 25%, 50% Ni
- Exported thermodynamic data (stress, strain) to text files for post-processing

### 2. Data Extraction and Processing
- Parsed stress-strain values from simulation output files
- Calculated **Young's Modulus** via linear regression over the elastic region
- Computed **Yield Strength** using the 0.2% offset method
- Determined **Ultimate Tensile Strength (UTS)** as peak stress before failure
- Compiled all results into a structured CSV dataset

### 3. Machine Learning
- **Model:** Random Forest Regressor
- **Input features:** Composition (% Ni), Temperature (K), Strain Rate
- **Output labels:** Young's Modulus, Yield Strength, UTS
- **Train/Test split:** 70% / 30%
- **Evaluation metrics:** Mean Absolute Error (MAE), R² Score
- Plotted actual vs. predicted graphs to visualize model behavior

---

## Results

### Mechanical Properties (Simulation Output)
| Property | Range |
|---|---|
| Young's Modulus | ~150 GPa – ~220 GPa |
| Yield Strength | ~0.26 GPa – ~1.0 GPa |
| UTS | up to ~1.3 GPa |

### ML Model Performance
| Property | MAE | R² |
|---|---|---|
| Young's Modulus | 30.264 | -2.240 |
| Yield Strength | 0.258 | -0.621 |
| UTS | 0.135 | -1.743 |

> **Note:** The negative R² scores are expected given the small dataset size (12 simulations, ~8 training samples). The model could identify directional trends but lacked sufficient data to generalize reliably. Expanding the simulation dataset is the primary next step.

### Feature Importance (Young's Modulus)
| Feature | Importance |
|---|---|
| Temperature | ~56% |
| Composition | ~26% |
| Strain Rate | ~18% |

---

## Key Findings
- Higher temperatures consistently reduced stiffness and strength across all compositions
- Increasing Ni content influenced both elastic and plastic behavior
- Temperature was the most dominant predictor in the ML model (~56% importance)
- The project demonstrates a viable pipeline for combining MD simulation data with ML — scalability is the main limitation at this stage

---

## Limitations
- Small dataset (12 simulations) limits ML generalization
- Results not yet validated against experimental literature
- Only Random Forest explored; other regressors may perform differently

---

## Future Work
- Expand simulation set (more Ni%, temperatures, strain rates) to 50+ data points
- Test Gradient Boosting, SVR, and neural network regressors
- Validate simulation trends against published experimental data
- Extend the framework to other alloy systems (e.g., Cu-Zn, Al-Mg)

---

## Tech Stack
- **Simulation:** LAMMPS, EAM Potential (CuNi.eam.alloy)
- **Data Processing:** Python (NumPy, Pandas)
- **Machine Learning:** Scikit-learn (Random Forest Regressor)
- **Visualization:** Matplotlib

## Acknowledgements
This project was completed as part of a course project at IIT Delhi, Department of Physics.
