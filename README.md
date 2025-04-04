# ML Potential Evaluation for Defect Formation Energy (Defective bilayer graphene system)

A Python-based evaluation framework for comparing different computational methods (DFT, machine learning potentials, and classical force fields) in predicting defect formation energies.
## Procedure
### Create Training Dataset
![Training dataset](/image/Training_Dataset.png)

**VASP Paramenter Setting**

**VOVO Bilayers**
1. Binding: AA, AB, SP (2.0 Å - 10.0 Å) (a)
2. Sliding: AB-stacked (3.2, 3.4, 3.6 Å) (a)
3. Deformation: 3% cell, ≤ 0.1 Å atomic shifts (a)
4. MD: Rebo-ILP (300K - 1500K) (b)

**VOV1 Bilayers**
AA, AB1, AB2 (3.4 Å, 63 atoms) (c)
1. Optimization: extract 1 in 5 steps
2. MD: AIMD at 300 K

**V1V1 Bilayers**
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

## Machine Learning Potential Models and Classical Force Fields for Defect Formation Energy Prediction

| Model/Force Field | Key Features | Reference |
|---|---|---|
| NequIP | Utilizes equivariant neural networks for accurate description of interatomic interactions. | ACS Nano 18, 10133-10141 (2024). |
| Deep Potential (DP) | Employs deep learning for efficient and accurate prediction of interatomic interactions. | ACS Nano 18, 10133-10141 (2024). |
| Neural Network Potential (NEP) | Fits potential energy surfaces using neural networks, suitable for complex systems. | ACS Nano 18, 10133-10141 (2024). |
| hNN-Grχ | Combines high-dimensional neural networks with graph-theoretic descriptors, applicable to complex materials. | Physical Review B 100, 195419 (2019). |
| GAP2020 | Based on Gaussian approximation potentials, accurately describes interactions of multiple elements. | Physical Review Letters 104, 136403 (2010). |
| AIREBO | Suitable for hydrocarbon systems, describes bond formation and breaking processes. | Journal of Chemical Physics 112, 6472-6486 (2000). |
| LCBOP | Applicable to silicon materials, describes covalent bond interactions. | Physical Review B 68, 024107 (2003). |
| Tersoff | Suitable for covalent bonded systems, describes bond angles and lengths. | Physical Review B 86, 115410 (2012). |
| ReaxFF | Applicable to reactive systems, describes interatomic interactions during chemical reactions. | The Journal of Physical Chemistry A 112, 1040-1053 (2008). |

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
