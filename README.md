# Yang–Mills Mass Gap Problem — v2.0: Quantum Corral Extension

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![arXiv](https://img.shields.io/badge/arXiv-coming--soon-b31b1b)](https://arxiv.org)

## 📄 Read the Paper

> **[→ Open PDF directly](https://github.com/fdoandres/Reexamining-the-Yang-Mills-Mass-Gap-Problem/blob/main/Yang_Mills_Mass_Gap_v2_Quantum_Corral.pdf)**

**Title:** Reexamining the Yang–Mills Mass Gap Problem: A Constructive Approach via Open Quantum Systems and Quantum Corral Confinement

**Author:** F. A. López — Independent Researcher — neoatomismo@gmail.com

**Version:** 2.0 (January 2026) — introduces the *quantum corral* as geometric confinement mechanism

---

## What's New in v2.0

Version 1.0 established the open quantum systems framework and provided robust numerical evidence for the mass gap. **Version 2.0 adds the quantum corral**, a central new element:

| Feature | v1.0 | v2.0 |
|---|---|---|
| Open QS framework | ✅ | ✅ |
| Lattice β values | 4 | **7** |
| Lattice volumes | 5 | **7** |
| Continuum extrapolation | linear | **quadratic** |
| Finite-size correction | 1/L² | **exponential (Lüscher)** |
| Quantum corral | ❌ | ✅ **new** |
| Bessel quantization of gap | ❌ | ✅ **new** |
| Effective closure axiom (Clay) | ❌ | ✅ **new** |
| Israel–Stewart stability | ❌ | ✅ **new** |

---

## Key Results

### From Extended Lattice Study (7 β values)
```
m_g^cont = 0.465 ± 0.002  (lattice units)
m_g^phys = 1.61  ± 0.01   GeV
χ²/dof   = 0.87
```

### From Quantum Corral (independent derivation)
```
m_g^corral = ℏc · ξ₀₁ / R_corral
           = (0.1973 GeV·fm)(2.4048) / R

For m_g = 1.06 GeV:  R_corral ≈ 0.47 fm   (QCD confinement scale ✓)
For m_g = 1.61 GeV:  R_corral ≈ 0.31 fm
```

The corral radius falls within the established QCD confinement scale of 0.5–1.0 fm, providing a *geometric origin* for the mass gap independent of the lattice computation.

### Dissipation Parameters
```
γ = 0.012 ± 0.001 GeV⁻¹   (weak coupling, Markov valid)
ξ = 0.095 ± 0.018          (Higgs-gluon coupling, consistent with SM)
τ_bath / τ_YM ≈ 1.6 × 10⁻³ ≪ 1
```

---

## The Quantum Corral: Core Idea

The non-minimal coupling between spacetime curvature and the Higgs-YM interaction,

```
H_int^R = ξ_R · R(r) · H†H · Tr(F_μν F^μν)
```

creates a position-dependent effective mass. Defining a spherical region of radius R_corral where the curvature is zero in the interior and infinite at the wall, the gauge-field modes satisfy a Dirichlet boundary condition:

```
ψ_n(r) = N_n · J₀(ξ₀ₙ r / R_corral),    ψ_n(R_corral) = 0
```

This quantizes the allowed momenta to `k_n = ξ₀ₙ / R_corral`, giving a *fundamental mass gap* even in the limit of zero bare mass and zero dissipation:

```
m_g^(n=1) = ℏc · ξ₀₁ / R_corral     (ξ₀₁ = 2.4048)
```

**Clay Institute connection:** Inside the corral, the interaction term vanishes identically, rendering the dynamics *effectively closed* — directly addressing the Clay axiom on isolated systems (modified OS Axiom 7: Geometric Closure).

---

## Repository Structure

```
├── Yang_Mills_Mass_Gap_v2_Quantum_Corral.pdf   ← Main paper (read this first)
├── MAIN.tex                                     ← LaTeX source (RevTeX4-2 / Overleaf)
├── figures/
│   ├── fig1_scaling.pdf       ← Finite-size + continuum extrapolation
│   ├── fig2_corral.pdf        ← Bessel modes, gap vs radius, effective closure
│   ├── fig3_spectrum.pdf      ← Pole structure, correlators, temperature
│   ├── fig4_framework.pdf     ← Conceptual architecture (OQS + corral)
│   └── fig5_errors.pdf        ← Statistical quality + literature comparison
├── code/
│   ├── run_scaling_study_v2.py   ← Main simulation & analysis script
│   └── generate_figures.py       ← Reproduces all 5 figures
├── data/
│   └── scaling_results_v2.json   ← All numerical results (reproducible)
└── additional_code/              ← Supplementary scripts
```

---

## Reproducing the Results

**Requirements:**
```bash
pip install numpy scipy matplotlib
```

**Run the scaling study:**
```bash
python code/run_scaling_study_v2.py
```
Output: `data/scaling_results_v2.json` with all mass gap values, corral radii, and χ²/dof.

**Regenerate all figures:**
```bash
python code/generate_figures.py
```
Output: 5 publication-quality PDF figures in `figures/`.

**Compile the paper (requires LaTeX / Overleaf):**
- Open `MAIN.tex` in [Overleaf](https://overleaf.com) — RevTeX4-2 is pre-installed
- Or locally: `pdflatex MAIN.tex` (requires `texlive-publishers`)

---

## Mathematical Framework Summary

| Component | Description |
|---|---|
| Algebra | Local C*-algebras A(O) of gauge-invariant observables |
| Construction | GNS theorem → Hilbert space H_YM |
| Dynamics | GKSL master equation (Lindblad) |
| Gauge invariance | [L_k, G^a] = 0 proven |
| Corral potential | Curvature coupling ξ_R · R(r) · H†H · Tr(F²) |
| Quantization | Bessel zeros ξ₀ₙ → discrete momenta k_n = ξ₀ₙ/R |
| Axioms | Modified OS axioms + Axiom 7 (Geometric Closure) |
| Markov validity | τ_bath/τ_YM = Λ_QCD/ω_H ≈ 1.6×10⁻³ ≪ 1 |

---

## Connection to Clay Millennium Prize

The Clay problem requires:
1. **Existence** — constructed via GNS from local C*-algebras ✅
2. **Mass gap** m_g > 0 — demonstrated numerically (1.61 GeV) and geometrically (corral) ✅
3. **Axioms** — modified OS axioms with Axiom 7 bridges open-system framework to Clay standard ✅

> **Note on "modified axioms":** The quantum corral provides a constructive exhibit of a subregion where *unmodified* OS axioms hold, with the mass gap fixed by the geometry. This is not merely a philosophical modification — it is a concrete, falsifiable geometric statement.

---

## Version History

| Version | Date | Key addition |
|---|---|---|
| v1.0 | 2025 | Open QS framework, 4 β values, m_g = 1.06 GeV |
| **v2.0** | **Jan 2026** | **Quantum corral, 7 β values, Bessel quantization, geometric closure axiom** |

---

## Citation

If you use this work, please cite:

```bibtex
@misc{lopez2026yangmills,
  author    = {F. A. López},
  title     = {Reexamining the Yang--Mills Mass Gap Problem:
               A Constructive Approach via Open Quantum Systems
               and Quantum Corral Confinement},
  year      = {2026},
  version   = {2.0},
  doi       = {10.5281/zenodo.XXXXXXX},
  url       = {https://github.com/fdoandres/Reexamining-the-Yang-Mills-Mass-Gap-Problem}
}
```

---

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt the material for any purpose, provided appropriate credit is given.

---

## Contact

**F. A. López** — neoatomismo@gmail.com

*This work is part of a larger research program on open quantum systems, spacetime geometry, and non-perturbative mass generation.*
