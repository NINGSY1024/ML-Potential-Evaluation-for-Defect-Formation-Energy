# ML Potential Evaluation for Defect Formation Energy

A Python-based evaluation framework for comparing different computational methods (DFT, machine learning potentials, and classical force fields) in predicting defect formation energies.
## Procedure
### Create Training Dataset
![Traning dataset](/image/Traing_Dataset.png)
### Results
![Force_RMSE](/image/Force_RMSE.png)
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
