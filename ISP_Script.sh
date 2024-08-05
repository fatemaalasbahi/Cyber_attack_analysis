#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --ntask=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --account=an-tr043
#SBATCH --output=isp_job_script_output.txt

module load python/3.11.5

virtualenv --no-download $SLURM_TIMDIR/env
source $SLURM_TIMDIR/env/bin/activate
pip install --no-index pandas numpy matplotlib seaborn re


python Cyber_analysis.py

deactivate
