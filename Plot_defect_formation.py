from pylab import *
from ase.io import read
from dpdata import LabeledSystem


# Set figure properties
aw = 2
fs = 18
lw = 2
ms = 8
font = {'size': fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes', lw=aw)
def set_fig_properties(ax_list):
    tl = 8
    tw = 2
    tlm = 4
    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='out', right=False, top=False)



def e_from_outcar(path): 
    ls = LabeledSystem(path, fmt = 'vasp/outcar')
    energy = ls[-1].data["energies"][0] # unit in eV
    return energy

def e_from_xyz(path):
    structure = read(path)
    energy = structure.info["energy"] # unit in eV
    return energy

def deltaE_outcar(path1, path2, n):
    e1 = e_from_outcar(path + path1 + "/DFT/OUTCAR")
    e2 = e_from_outcar(path + path2 + "/DFT/OUTCAR")
    return e2 - e1*n

def deltaE_xyz(path1, path2, label, n):
    e1 = e_from_xyz(path + path1 + f"/model_{label}_optimize.xyz")
    e2 = e_from_xyz(path + path2 + f"/model_{label}_optimize.xyz")
    return e2 - e1*n

def deltaE_lammps(path1, path2, label, n):
    e1 = loadtxt(path + path1 + f"/LAMMPS/{label}_energy.data")[-1]
    e2 = loadtxt(path + path2 + f"/LAMMPS/{label}_energy.data")[-1]
    return e2 - e1*n

path = "./"

fig=figure(figsize=(20, 10))
dft_v1 = deltaE_outcar("V0", "V1", 1)
nequip_v1 = deltaE_xyz("V0", "V1", "nequip", 1)
dp_v1 = deltaE_xyz("V0", "V1", "dp", 1)
nep_v1 = deltaE_xyz("V0", "V1", "nep", 1)
gap2020_v1 = deltaE_xyz("V0", "V1", "gap2020", 1)
hnngrx_v1 = deltaE_xyz("V0", "V1", "hnn-grx", 1)
airebo_v1 = deltaE_lammps("V0", "V1", "airebo", 1)
tersoff_v1 = deltaE_lammps("V0", "V1", "tersoff", 1)
lcbop_v1 = deltaE_lammps("V0", "V1", "LCBOP", 1)
reaxff_v1 = deltaE_lammps("V0", "V1", "ReaxFF", 1)*0.043 #from Kcal/mol to eV

labels = ['DFT', 'NequIP', 'DP', 'NEP', 'GAP2020', r'hNN-Gr$_{\chi}$', 
          'AIREBO', 'Tersoff', 'LCBOP', 'ReaxFF'][::-1]
data   = [dft_v1, nequip_v1, dp_v1, nep_v1, gap2020_v1, hnngrx_v1, 
        airebo_v1, tersoff_v1, lcbop_v1, reaxff_v1][::-1]


subplot(1, 4, 1)
set_fig_properties([gca()])
height = 0.6
bar_positions = range(len(labels))  # Define bar positions
for i in range(len(labels)):
    if labels[i] == 'DFT':
        barh(bar_positions[i], data[i], height, color="C3")
    elif labels[i] == 'NequIP':
        barh(bar_positions[i], data[i], height, color="C1")
    elif labels[i] in ['DP', 'NEP', 'GAP2020', r'hNN-Gr$_{\chi}$']:
        barh(bar_positions[i], data[i], height, color="C0")
    else:
        barh(bar_positions[i], data[i], height, color="C2")
    text(data[i]+0.6, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
xlim([6, 26])
gca().set_xticks(linspace(6, 24, 4))
ylim([-0.5, 9.5])
gca().set_yticks(linspace(0, 9, 10))
gca().set_yticklabels(labels)
xlabel('Formation energy (eV)')
title(r"(a) V$_1")


dft_AB1 = deltaE_outcar("V1", "AB1", 2)
nequip_AB1 = deltaE_xyz("V1", "AB1", "nequip", 2)
dp_AB1 = deltaE_xyz("V1", "AB1", "dp", 2)
nep_AB1 = deltaE_xyz("V1", "AB1", "nep", 2)
gap2020_AB1 = deltaE_xyz("V1", "AB1", "gap2020", 2)
hnngrx_AB1 = deltaE_xyz("V1", "AB1", "hnn-grx", 2)
airebo_AB1 = deltaE_lammps("V1", "AB1", "airebo", 2)
tersoff_AB1 = deltaE_lammps("V1", "AB1", "tersoff", 2)
lcbop_AB1 = deltaE_lammps("V1", "AB1", "LCBOP", 2)
reaxff_AB1 = deltaE_lammps("V1", "AB1", "ReaxFF", 2)*0.043 #from Kcal/mol to eV
data = [dft_AB1, nequip_AB1, dp_AB1, nep_AB1, gap2020_AB1, hnngrx_AB1,
        airebo_AB1, tersoff_AB1, lcbop_AB1, reaxff_AB1][::-1]
subplot(1, 4, 2)
set_fig_properties([gca()])
bar_positions = range(len(labels))  # Define bar positions
barh(bar_positions[-1], data[-1], height, color="C3")
barh(bar_positions[-2], data[-2], height, color="C1")
barh(bar_positions[:-2], data[:-2], height, color="C0")
for i in range(len(labels)):
    if labels[i] == 'DFT':
        barh(bar_positions[i], data[i], height, color="C3")
    elif labels[i] == 'NequIP':
        barh(bar_positions[i], data[i], height, color="C1")
    elif labels[i] in ['DP', 'NEP', 'GAP2020', r'hNN-Gr$_{\chi}$']:
        barh(bar_positions[i], data[i], height, color="C0")
    else:
        barh(bar_positions[i], data[i], height, color="C2")
        
    if labels[i] != 'Tersoff':
        text(data[i]-6, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
    else:
        text(data[i]+0.8, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
vlines(0, -0.5, 9.5, lw=lw-0.5, color="black")
xlim([-20, 15])
gca().set_xticks(linspace(-12, 12, 5))
ylim([-0.5, 9.5])
gca().set_yticks([])
xlabel('Formation energy (eV)')
title("(b) ABI")

dft_AB2 = deltaE_outcar("V1", "AB2", 2)
nequip_AB2 = deltaE_xyz("V1", "AB2", "nequip", 2)
dp_AB2 = deltaE_xyz("V1", "AB2", "dp", 2)
nep_AB2 = deltaE_xyz("V1", "AB2", "nep", 2)
gap2020_AB2 = deltaE_xyz("V1", "AB2", "gap2020", 2)
hnngrx_AB2 = deltaE_xyz("V1", "AB2", "hnn-grx", 2)
airebo_AB2 = deltaE_lammps("V1", "AB2", "airebo", 2)
tersoff_AB2 = deltaE_lammps("V1", "AB2", "tersoff", 2)
lcbop_AB2 = deltaE_lammps("V1", "AB2", "LCBOP", 2)
reaxff_AB2 = deltaE_lammps("V1", "AB2", "ReaxFF", 2)*0.043 #from Kcal/mol to eV
data = [dft_AB2, nequip_AB2, dp_AB2, nep_AB2, gap2020_AB2, hnngrx_AB2,
        airebo_AB2, tersoff_AB2, lcbop_AB2, reaxff_AB2][::-1]
subplot(1, 4, 3)
set_fig_properties([gca()])
bar_positions = range(len(labels))  # Define bar positions
for i in range(len(labels)):
    if labels[i] == 'DFT':
        barh(bar_positions[i], data[i], height, color="C3")
    elif labels[i] == 'NequIP':
        barh(bar_positions[i], data[i], height, color="C1")
    elif labels[i] in ['DP', 'NEP', 'GAP2020', r'hNN-Gr$_{\chi}$']:
        barh(bar_positions[i], data[i], height, color="C0")
    else:
        barh(bar_positions[i], data[i], height, color="C2")
        
    if labels[i] != 'Tersoff':
        text(data[i]-4.5, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
    else:
        text(data[i]+0.8, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
vlines(0, -0.5, 9.5, lw=lw-0.5, color="black")
xlim([-18, 8])
gca().set_xticks(linspace(-15, 5, 5))
ylim([-0.5, 9.5])
gca().set_yticks([])
xlabel('Formation energy (eV)')
title("(c) ABII")

dft_AA3 = deltaE_outcar("V1", "AA3", 2)
nequip_AA3 = deltaE_xyz("V1", "AA3", "nequip", 2)
dp_AA3 = deltaE_xyz("V1", "AA3", "dp", 2)
nep_AA3 = deltaE_xyz("V1", "AA3", "nep", 2)
gap2020_AA3 = deltaE_xyz("V1", "AA3", "gap2020", 2)
hnngrx_AA3 = deltaE_xyz("V1", "AA3", "hnn-grx", 2)
airebo_AA3 = deltaE_lammps("V1", "AA3", "airebo", 2)
tersoff_AA3 = deltaE_lammps("V1", "AA3", "tersoff", 2)
lcbop_AA3 = deltaE_lammps("V1", "AA3", "LCBOP", 2)
reaxff_AA3 = deltaE_lammps("V1", "AA3", "ReaxFF", 2)*0.043 #from Kcal/mol to eV
data = [dft_AA3, nequip_AA3, dp_AA3, nep_AA3, gap2020_AA3, hnngrx_AA3,
        airebo_AA3, tersoff_AA3, lcbop_AA3, reaxff_AA3][::-1]
subplot(1, 4, 4)
set_fig_properties([gca()])
bar_positions = range(len(labels))  # Define bar positions
for i in range(len(labels)):
    if labels[i] == 'DFT':
        barh(bar_positions[i], data[i], height, color="C3")
    elif labels[i] == 'NequIP':
        barh(bar_positions[i], data[i], height, color="C1")
    elif labels[i] in ['DP', 'NEP', 'GAP2020', r'hNN-Gr$_{\chi}$']:
        barh(bar_positions[i], data[i], height, color="C0")
    else:
        barh(bar_positions[i], data[i], height, color="C2")
        
    if labels[i] != 'Tersoff':
        text(data[i]-6.5, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
    else:
        text(data[i]+0.5, bar_positions[i], "{:.1f}".format(data[i]), va='center', fontsize=fs)
vlines(0, -0.5, 9.5, lw=lw-0.5, color="black")
xlim([-24, 12])
gca().set_xticks(linspace(-20, 10, 4))
ylim([-0.5, 9.5])
gca().set_yticks([])
xlabel('Formation energy (eV)')
title("(d) AAIII")
subplots_adjust(wspace=0.05)
savefig("defect_formation.png", bbox_inches='tight')


dft = np.array([dft_v1, dft_AB1, dft_AB2, dft_AA3])
nequip = np.array([nequip_v1, nequip_AB1, nequip_AB2, nequip_AA3])
dp = np.array([dp_v1, dp_AB1, dp_AB2, dp_AA3])
nep = np.array([nep_v1, nep_AB1, nep_AB2, nep_AA3])
gap2020 = np.array([gap2020_v1, gap2020_AB1, gap2020_AB2, gap2020_AA3])
hnngrx = np.array([hnngrx_v1, hnngrx_AB1, hnngrx_AB2, hnngrx_AA3])
airebo = np.array([airebo_v1, airebo_AB1, airebo_AB2, airebo_AA3])
tersoff = np.array([tersoff_v1, tersoff_AB1, tersoff_AB2, tersoff_AA3])
lcbop = np.array([lcbop_v1, lcbop_AB1, lcbop_AB2, lcbop_AA3])
reaxff = np.array([reaxff_v1, reaxff_AB1, reaxff_AB2, reaxff_AA3])

output_string = ""
labels = ['NequIP', 'DP', 'NEP', 'GAP2020', r'hNN-Gr$_{\chi}$', 
          'AIREBO', 'Tersoff', 'LCBOP', 'ReaxFF']
mlps = [nequip, dp, nep, gap2020, hnngrx, airebo, tersoff, lcbop, reaxff] 
for i in range(len(mlps)):
    l = labels[i]
    m = mlps[i]
    rmse = np.sqrt(sum((m - dft) ** 2) / len(dft)) 
    prompt = f"Energy RMSE of formation energy predicted by {l} is {rmse:.1f} eV.\n"
    print(prompt)
    output_string += prompt

with open("Defect.log", "w") as f:
    f.write(output_string)