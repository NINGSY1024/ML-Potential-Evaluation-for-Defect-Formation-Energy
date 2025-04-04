# ML Potential Evaluation for Defect Formation Energy (Defective bilayer graphene system)

A Python-based evaluation framework for comparing different computational methods (DFT, machine learning potentials, and classical force fields) in predicting defect formation energies.
## Procedure
### Create Training Dataset
![Training dataset](/image/Training_Dataset.png)
**VASP Paramenter Setting**
V0V0 Bilayers
1. Binding: AA, AB, SP (2.0 Å - 10.0 Å) (a)
2. Sliding: AB-stacked (3.2, 3.4, 3.6 Å) (a)
3. Deformation: 3% cell, ≤ 0.1 Å atomic shifts (a)
4. MD: Rebo-ILP (300K - 1500K) (b) o V0V1 Bilayers
AA, AB1, AB2 (3.4 Å, 63 atoms) (c)
1. Optimization: extract 1 in 5 steps
2. MD: AIMD at 300 K o V1V1 Bilayers
AA, AB1, AB2 (2.0, 2.5, 3.0 Å; 62 atoms) (c)
1. Optimization: extract every step
2. MD: AIMD (300K, 900K, 1500K)
### MD Simulations
![MD](/image/MD_Simulation.png)

### Force RMSE
![Force_RMSE](/image/Force_RMSE.png)

### Defect Formation Energy
![E_F](/image/Defect_Formation_Energy.png)
## Features

- **Multiple Computational Methods Support**:
  - DFT (VASP)
  - Machine Learning Potentials (NequIP, Deep Potential, NEP, GAP2020, hNN-Grχ)
  - Classical Force Fields (AIREBO, Tersoff, LCBOP, ReaxFF)

- **Defect Types**:
  - Pristine (V0)
  - Single Vacancy (V1)
  - AB-type Defects (AB1, AB2)
  - AA-type Defects (AA3)

- **Analysis Tools**:
  - Automated energy calculation
  - RMSE analysis
  - Visualization with matplotlib
  - Performance comparison

## Directory Structure

## Usage

1. Place your calculation results in the corresponding directories following the structure:
   - DFT results: `{defect}/DFT/OUTCAR`
   - ML potential results: `{defect}/model_{label}_optimize.xyz`
   - Force field results: `{defect}/LAMMPS/{label}_energy.data`

2. Run the analysis script:
   ```bash
   python Plot_defect_formation.py
   ```

3. Check the results:
   - Visualization: `defect_formation.png`
   - Performance metrics: `Defect.log`

## Adding New Methods

To add a new computational method:

1. Add your calculation results following the existing directory structure
2. Add a new entry in the `labels` list
3. Add corresponding energy calculations using the existing functions

## Dependencies

- Python 3.x
- ASE (Atomic Simulation Environment)
- dpdata
- matplotlib
- numpy
