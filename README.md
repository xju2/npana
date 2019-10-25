# Introduction 
Column-wise High Energy Physics Analysis Package

# Installation
```bash
conda create --name numpyana python=3.7
conda activate numpyana
conda install -c conda-forge jupyterlab
conda install -c conda-forge root

```
Load the cuda module for GPU usage
```
module load cuda/10.1.168
```

Now start to install the package
```
git clone https://github.com/xju2/npana
cd npana
pip install -e .

```
