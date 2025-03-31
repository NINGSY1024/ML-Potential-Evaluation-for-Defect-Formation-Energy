#!/bin/bash
#PBS -N AB1_opt
#PBS -q power-chemistry
#PBS -l nodes=1:ppn=48,walltime=2400:00:00
#PBS -l mem=96gb 
#PBS -r n

#module load mpi/openmpi-3.1.0-intel
module load intel/parallel_studio_xe_2018
#module load mpi/openmpi-3.1.0-intel
#module load intel/parallel_studio_xe_2019
export LD_LIBRARY_PATH=/powerapps/share/intel/parallel_studio_xe_2018/compilers_and_libraries_2018.1.163/linux/compiler/lib/intel64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/powerapps/share/intel/parallel_studio_xe_2018/compilers_and_libraries_2018.1.163/linux/mpi/intel64/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/powerapps/share/intel/parallel_studio_xe_2018/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64:$LD_LIBRARY_PATH
#export LD_LIBRARY_PATH=/powerapps/share/intel/parallel_studio_xe_2018/compilers_and_libraries_2018.1.163/linux/tbb/lib/intel64_lin/gcc4.7/:$LD_LIBRARY_PATH

export OMP_NUM_THREADS=1
cd $PBS_O_WORKDIR
export NPROC=48

cp ../DFT/CONTCAR POSCAR
echo -e "103" |vaspkit
mpiexec -np $NPROC /a/home/cc/chemist/hityingph/bin/vasp/vasp.5.4.4/bin/vasp_std 
