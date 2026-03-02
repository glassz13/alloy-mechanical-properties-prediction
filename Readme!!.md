Project: Predicting Mechanical Properties of Cu-Ni Alloys Using Molecular Dynamics and Machine Learning

Aim:
The main goal was to see how composition, temperature, and strain rate affect the mechanical behavior of Cu-Ni alloys. I used LAMMPS simulations to generate stress-strain data and applied machine learning to predict material properties.

Methodology:

1. Simulation:
   - Created FCC lattice models with different nickel content (0%, 25%, 50%).
   - Used the EAM potential file (CuNi.eam.alloy) to define interactions.
   - Applied initial velocities and equilibrated systems using NPT ensemble.
   - Performed uniaxial tensile deformation by deforming the simulation box along the z-axis.
   - Ran 12 simulations combining:
        - Temperatures: 300K and 500K
        - Strain rates: 0.001 and 0.0005
        - Compositions: 0%, 25%, 50% Ni
   - Saved thermodynamic data to text files. 
   -extract stress vs strain data from text file to plot graphs and do calculations.

2. Data Extraction and Processing:
   - Parsed stress and strain values from the simulation outputs.
   - Calculated Young's Modulus by linear fitting of the elastic region of the stress-strain curve.
   - Computed Yield Strength using the 0.2% offset method.
   - Determined Ultimate Tensile Strength as the peak stress before failure.
   - Compiled all results into a CSV dataset.

3. Machine Learning:
   - Encoded categorical composition data as numeric.
   - Prepared input features: Composition (%Ni), Temperature (K), Strain Rate.
   - Output labels: Young's Modulus, Yield Strength, UTS.
   - Used Random Forest Regressor as the predictive model.
   - Split the data into training and test sets (70% train, 30% test).
   - Evaluated performance using Mean Absolute Error and R2 Score.
   - Plotted actual vs predicted graphs to check how well the model captured trends.

Main Results:

Final Mechanical Properties (example ranges):
- Young's Modulus varied from ~150 GPa to ~220 GPa (some outliers higher).
- Yield Strength ranged between ~0.26 GPa and ~1 GPa.
- UTS values reached up to ~1.3 GPa.

Model Performance:
Young's Modulus:
  MAE: 30.264
  R2: -2.240

Yield Strength:
  MAE: 0.258
  R2: -0.621

UTS:
  MAE: 0.135
  R2: -1.743

Feature Importance (Young's Modulus Prediction):
- Temperature: ~56%
- Composition: ~26%
- Strain Rate: ~18%

Interpretation:
The results show that temperature and composition have a significant influence on elastic modulus and strength. Higher temperatures generally reduce stiffness and strength. The machine learning model was able to identify some patterns but had limited accuracy, mainly due to the small dataset size. This approach demonstrates how simulation data can be combined with ML tools to estimate mechanical properties without needing experimental measurements.

Way Forward:
- Increasing the number of simulations to create a bigger dataset.
- Trying other regression algorithms like Gradient Boosting or SVR.
- Comparing simulation results with literature data to validate trends more accurately.
- Extending this framework to other alloy systems.

