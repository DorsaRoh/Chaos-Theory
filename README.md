
# 3D Chaos Theory

### The computation of 3D chaotic dynamical systems.


<p align="center">
<img width="800px" src="assets\3d_lorenz.png">
<img width="850px" src="assets\XYZPlanes.png">
<img width="600px" src="assets\LogisticMap.png">
</p>

## Features:
- Computes and graphs Lorenz Attractors using values sigma, beta, Rho and time inputted by the user. 
- Trajectory curve graphs, XY, YZ and XZ axis matplotlib graph visuals.
- Logistic Map using an inputted value for the r axis. Bifurcation can be controlled by the number of iterations given by the user.

## Installation

### 1. Clone the repository
```shell
git clone https://github.com/DorsaRoh/https://github.com/DorsaRoh/Chaos-Theory
```

```shell
cd Chaos-Theory
```

### 2. Install dependencies
```shell
pip install numpy matplotlib scipy
```
or
```shell
pip install -r requirements.txt
```

### 3. Usage

Enter your parameters in **parameters.py** file

**Lorenz Attractor**
- sigma (default: 10.0) 
- rho (default: 28.0)
- beta (default 8.0/3)

**Logistic Map**
- inv (default: 2.4)
- endv (default: 4.0)
