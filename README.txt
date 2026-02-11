# Dissipative Yang-Mills Mass Gap Study

This repository contains all materials for the paper:
"Reexamining the Yang--Mills Mass Gap Problem: A Constructive Approach via Open Quantum Systems with Robust Numerical Evidence and Emergent Gravity"

## Contents

### 1. LaTeX Document
- `main.tex`: Complete LaTeX source of the paper

### 2. Figures (PDF and PNG)
- `finite_size_scaling.pdf`: Figure 1 - Finite-size scaling
- `continuum_extrapolation.pdf`: Figure 2 - Continuum extrapolation
- `error_analysis.pdf`: Figure 3 - Error analysis
- `KAN_extrapolation.pdf`: Figure 4 - KAN-based extrapolation
- `emergent_gravity.pdf`: Figure 5 - Emergent gravity schematic

### 3. Python Code
- `run_scaling_study.py`: Main execution script
- `KAN_analysis.py`: KAN implementation with modular regularization

### 4. Data
- `scaling_results.json`: Numerical results used in the paper

### 5. Reproduction Instructions

1. Install dependencies:
   pip install numpy scipy matplotlib

2. Run the scaling study:
   python code/run_scaling_study.py

3. Generate figures:
   The figures are already provided in the figures/ directory.

## Key Results

- Continuum mass gap: m_g^cont = 0.467 ± 0.003 (lattice units)
- Physical glueball mass: m_g^phys = 1.62 ± 0.01 GeV
- Dissipative coefficient: gamma = 0.012 ± 0.002
- All figures use Times New Roman font for publication quality

## Contact
F. A. López - neoatomismo@gmail.com
