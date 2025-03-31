from ase.io import read, write
from ase.constraints import ExpCellFilter
from ase.optimize import BFGS, FIRE, GPMin
from ase.optimize.sciopt import SciPyFminBFGS
from ase import Atoms


label = "nequip"
from nequip.ase.nequip_calculator import NequIPCalculator
calc = NequIPCalculator.from_deployed_model(model_path = "/yinglab/Reactive_ILP/MLP/NequIP/deployed.pth", device='cuda')
structure = read("DFT/CONTCAR")
structure.set_calculator(calc)
print(structure.get_potential_energies())
write(f"model_{label}_no_optimize.xyz", structure)
