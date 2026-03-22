# Changelog

All notable changes to this research are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.0] — 2026-01-11

### Added
- **Quantum Corral** (Sec. 3): new geometric confinement mechanism
  based on non-minimal curvature coupling `ξ_R · R(r) · H†H · Tr(F²)`.
- **Bessel quantization** (Proposition 3.1): allowed momenta
  `k_n = ξ₀ₙ / R_corral`, fundamental mode gives
  `m_g = ℏc · ξ₀₁ / R_corral`.
- **Corral radius calculation** (Table 1, Sec. 3.4): `R_corral ≈ 0.47 fm`
  for `m_g = 1.06 GeV`; consistent with QCD confinement scale.
- **Israel–Stewart stability** (Sec. 3.5): relaxation time
  `τ_π ~ R_corral/c` ensures gap is dynamically stable equilibrium.
- **Modified OS Axiom 7 — Geometric Closure** (Sec. 7): constructive
  exhibit of subregion where unmodified Clay axioms hold.
- **Remark 3.2 (Effective Closure)**: addresses Clay closed-system
  objection directly.
- Three new β values: β = 6.5, 6.8, 7.0 (total: 7 values).
- Two new volumes: L = 40, 48 (total: 7 volumes).
- Exponential Lüscher finite-size correction form.
- Quadratic continuum extrapolation (preferred by AIC/BIC).
- References: Birrell & Davies (1982), Crommie et al. (1993),
  Israel & Stewart (1979).
- Figure 2 (corral geometry), Figure 4 (framework architecture) — new.
- `generate_figures.py` — all 5 figures reproducible from code.
- `CITATION.cff` — standard citation metadata.
- `scaling_results_v2.json` — full numerical output.

### Changed
- Continuum limit: `0.467 ± 0.003` → `0.465 ± 0.002` (more β values).
- Physical mass: `1.06 ± 0.01 GeV` → `1.61 ± 0.01 GeV`
  (corrected conversion using asymptotic scaling for all 7 β).
- Finite-size correction form: `A/L²` → `A·exp(-m_g L)/L`
  (Lüscher exponential, better χ²/dof: 1.8 → 0.87).
- Abstract expanded to include quantum corral and Clay bridge.
- Section structure: 8 sections → 9 sections (Sec. 3 = Quantum Corral new).

### Fixed
- Continuum extrapolation now uses quadratic fit (linear was underfitting
  at fine lattice spacings).

---

## [1.0] — 2025

### Initial release
- Open quantum systems framework for Yang-Mills theory.
- Local C*-algebras, GNS construction, GKSL master equation.
- Schwinger-Keldysh formalism; infrared propagator parameterization.
- Lattice study: β ∈ {5.7, 5.9, 6.1, 6.3}, L ∈ {8, 12, 16, 24, 32}.
- Continuum result: `m_g = 0.467 ± 0.003` (latt.), `1.06 ± 0.01 GeV`.
- Modified OS axioms (6 axioms).
- Physical interpretation: Higgs field as environment.
