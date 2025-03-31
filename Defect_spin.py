from pylab import *
from ase.io import read
from glob import glob
from dpdata import LabeledSystem,MultiSystems


# Set figure properties
aw = 1.5
fs = 16
lw = 1.5
ms = 6
font = {'size': fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes', lw=aw)
def set_fig_properties(ax_list):
    tl = 6
    tw = 1.5
    tlm = 3
    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='out', right=False, top=False)


def e_from_outcar(path): 
    ls = LabeledSystem(path, fmt = 'vasp/outcar')
    energy = ls[-1].data["energies"][0] # unit in eV
    # energy = ls[-1].data["energies"] / len(ls[-1].data["coords"][0]) # unit in eV/atom
    return energy

def e_from_xyz(path):
    structure = read(path)
    energy = structure.info["energy"] # unit in eV
    return energy

path = "./"
dft_v0 = e_from_outcar(path + "V0/DFT/OUTCAR")
spin_v0 = e_from_outcar(path + "V0/DFT_spin/OUTCAR")
dft_v1 = e_from_outcar(path + "V1/DFT/OUTCAR")
spin_v1 = e_from_outcar(path + "V1/DFT_spin/OUTCAR")
dft_delta_v1 = dft_v1 - dft_v0
spin_delta_v1 = spin_v1 - spin_v0

dft_ab1 = e_from_outcar(path + "AB1/DFT/OUTCAR")
dft_delta_ab1 = dft_ab1 - 2*dft_v1
spin_ab1 = e_from_outcar(path + "AB1/DFT_spin/OUTCAR")
spin_delta_ab1 = spin_ab1 - 2*spin_v1

dft_ab2 = e_from_outcar(path + "AB2/DFT/OUTCAR")
dft_delta_ab2 = dft_ab2 - 2*dft_v1
spin_ab2 = e_from_outcar(path + "AB2/DFT_spin/OUTCAR")
spin_delta_ab2 = spin_ab2 - 2*spin_v1

dft_aa3 = e_from_outcar(path + "AA3/DFT/OUTCAR")
dft_delta_aa3 = dft_aa3 - 2*dft_v1
spin_aa3 = e_from_outcar(path + "AA3/DFT_spin/OUTCAR")
spin_delta_aa3 = spin_aa3 - 2*spin_v1



dft_deltas = [dft_delta_v1, dft_delta_ab1, dft_delta_ab2, dft_delta_aa3][::-1]  # Reverse the order
spin_deltas = [spin_delta_v1, spin_delta_ab1, spin_delta_ab2, spin_delta_aa3][::-1]  # Reverse the order
labels = [r'V$_1$', 'AB\u2160', 'AB\u2161', 'AA\u2162'][::-1]  # Reverse the order of labels
y = np.arange(len(labels))  # the label locations
height = 0.35  # the height of the bars
fig = figure(figsize=(6, 8))
set_fig_properties([gca()])
rects1 = barh(y + height/2, dft_deltas, height, color='C3', label='Non-spin-polarized')
rects2 = barh(y - height/2, spin_deltas, height, color='C1', hatch='x', edgecolor="white", label='Spin-polarized')
ylim([-0.5, 3.5])
xlim([-12, 25])
gca().set_xticks(np.linspace(-10, 20, 4))
vlines(0, -2, 6, colors="grey", lw=1.5)
gca().set_xlabel(r'Formation energy (eV)')
gca().set_yticks(y)
gca().set_yticklabels(labels)
legend(frameon=False)
def autolabel(rects):
    """Attach a text label beside each bar in *rects*, displaying its width."""
    for rect in rects:
        width = rect.get_width()
        gca().annotate('{:.2f}'.format(width),
                    xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(-12, 0) if width < 0 else (3, 0),  # Adjusted horizontal offset for negative values
                    textcoords="offset points",
                    va='center', ha='right' if width < 0 else 'left')
autolabel(rects1)  # For DFT
autolabel(rects2)  # For spin
# fig.text(0, 0.5, r"$\Delta E$ (eV)", va='center', rotation='vertical')
savefig("Defect_spin.svg", bbox_inches='tight')

