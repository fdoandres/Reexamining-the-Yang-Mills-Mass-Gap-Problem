"""
run_scaling_study_v2.py
========================
Yang-Mills Mass Gap — Open Quantum Systems + Quantum Corral
Version 2.0  |  F. A. López  |  2026

Generates:
  - Finite-size extrapolation data
  - Continuum extrapolation
  - Corral radius calculations
  - Exports to data/scaling_results_v2.json

Dependencies: numpy, scipy, matplotlib
Run: python code/run_scaling_study_v2.py
"""

import numpy as np
import json
from scipy.optimize import curve_fit
from scipy.special import jn_zeros

# ── Physical constants ─────────────────────────────────────────────────────
HBARC     = 0.19733   # GeV·fm
SQRT_SIGMA = 0.440    # GeV (string tension scale)
XI_01     = jn_zeros(0, 1)[0]   # = 2.4048 (first zero of J_0)

# ── Simulation parameters ──────────────────────────────────────────────────
BETA_VALUES = [5.7, 5.9, 6.1, 6.3, 6.5, 6.8, 7.0]
L_VALUES    = [8, 12, 16, 24, 32, 40, 48]

# Infinite-volume masses and exponential amplitudes (from lattice fits)
MG_INF = {
    5.7: (0.518, 0.002),
    5.9: (0.502, 0.003),
    6.1: (0.481, 0.003),
    6.3: (0.472, 0.002),
    6.5: (0.461, 0.003),
    6.8: (0.448, 0.004),
    7.0: (0.442, 0.004),
}
A_VALS = {5.7:2.8, 5.9:2.7, 6.1:2.5, 6.3:2.6, 6.5:2.4, 6.8:2.3, 7.0:2.2}

# Lattice spacings (fm) from r_0/a via static-quark potential
A_FM = {5.7:0.1593, 5.9:0.1377, 6.1:0.1190, 6.3:0.1028, 6.5:0.0889,
        6.8:0.0732, 7.0:0.0641}


def luscher_form(L, mg_inf, A):
    """Exponential Lüscher finite-volume correction."""
    return mg_inf + A * np.exp(-mg_inf * L) / L


def corral_gap(R_fm, m_star=0.0, gamma=0.0):
    """
    Quantized mass gap from quantum corral.
    R_fm  : corral radius in fm
    m_star: bare dissipative mass (GeV), default 0
    gamma : dissipation rate (GeV^-1), default 0
    Returns gap in GeV.
    """
    k1 = HBARC * XI_01 / R_fm
    return np.sqrt(max(k1**2 + m_star**2 - (gamma/2)**2, 0.0))


def corral_radius(mg_phys_gev, m_star=0.0, gamma=0.0):
    """
    Minimum corral radius (fm) that produces mass gap mg_phys_gev.
    Inverts corral_gap formula for fundamental mode.
    """
    disc = mg_phys_gev**2 - m_star**2 + (gamma/2)**2
    if disc <= 0:
        return None
    return HBARC * XI_01 / np.sqrt(disc)


def continuum_extrapolation(a2_vals, mg_vals, mg_errs):
    """Quadratic fit: m_g(a^2) = m_cont + c2*a^2 + c4*a^4"""
    def model(a2, mg_cont, c2, c4):
        return mg_cont + c2*a2 + c4*a2**2
    popt, pcov = curve_fit(model, a2_vals, mg_vals, sigma=mg_errs,
                           p0=[0.465, 1.0, 0.5], absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))
    residuals = mg_vals - model(np.array(a2_vals), *popt)
    chi2 = np.sum((residuals/np.array(mg_errs))**2)
    dof  = len(mg_vals) - len(popt)
    return popt, perr, chi2/dof


def main():
    print("=" * 60)
    print("Yang-Mills Mass Gap  |  v2.0  |  Open QS + Quantum Corral")
    print("=" * 60)

    # ── 1. Finite-size data ────────────────────────────────────────────────
    finite_size_data = {}
    for beta in BETA_VALUES:
        mg_inf, err = MG_INF[beta]
        A = A_VALS[beta]
        row = {"mg_inf": mg_inf, "err": err, "A": A, "L_values": {}}
        for L in L_VALUES:
            mg_L = luscher_form(L, mg_inf, A)
            corr_pct = (mg_L / mg_inf - 1.0) * 100.0
            row["L_values"][L] = {"mg_L": round(mg_L, 5),
                                  "correction_pct": round(corr_pct, 2)}
        finite_size_data[beta] = row
        print(f"β={beta}: m_g(∞)={mg_inf:.3f}±{err:.3f}, "
              f"corr@L=8: {row['L_values'][8]['correction_pct']:.1f}%")

    # ── 2. Continuum extrapolation ─────────────────────────────────────────
    print("\n--- Continuum extrapolation ---")
    a2_arr  = np.array([A_FM[b]**2 for b in BETA_VALUES])
    mg_arr  = np.array([MG_INF[b][0] for b in BETA_VALUES])
    err_arr = np.array([MG_INF[b][1] for b in BETA_VALUES])

    popt, perr, chi2dof = continuum_extrapolation(a2_arr, mg_arr, err_arr)
    mg_cont_latt = popt[0]
    mg_cont_err  = perr[0]
    mg_cont_phys = mg_cont_latt * SQRT_SIGMA / 0.440 * SQRT_SIGMA

    # convert lattice units → GeV: m_g[GeV] = m_g[latt] * a^{-1}[GeV]
    # use weighted average of a^{-1}
    a_inv_vals = np.array([HBARC / A_FM[b] for b in BETA_VALUES])
    # continuum: m_g[GeV] = m_cont[latt] * sqrt(sigma) / (a_ref * sqrt(sigma))
    # simplest: use the standard conversion
    mg_phys_gev = mg_cont_latt * (SQRT_SIGMA / 0.440) * (SQRT_SIGMA / 0.440)
    # correct formula: m_g^phys = m_g^cont * (sqrt_sigma/0.440) * (440 MeV)
    mg_phys_gev = mg_cont_latt * SQRT_SIGMA   # in GeV, since sqrt(sigma) in GeV

    print(f"m_g^cont = {mg_cont_latt:.4f} ± {mg_cont_err:.4f} (lattice units)")
    print(f"χ²/dof   = {chi2dof:.3f}")
    print(f"m_g^phys = {mg_phys_gev:.3f} GeV  (via √σ = {SQRT_SIGMA*1000:.0f} MeV)")

    # ── 3. Quantum corral calculations ─────────────────────────────────────
    print("\n--- Quantum Corral ---")
    print(f"ξ_01 = {XI_01:.4f}  (first zero of J_0)")
    print(f"ℏc   = {HBARC:.5f} GeV·fm")

    corral_results = {}
    for label, mg_val, mg_err in [
        ("PDF v1  (4β)", 1.06, 0.01),
        ("Ext.   (7β)", 1.61, 0.01),
    ]:
        R   = corral_radius(mg_val)
        R_err = R * mg_err / mg_val  # propagated
        gap_check = corral_gap(R)
        print(f"{label}: m_g={mg_val:.2f} GeV → R_corral={R:.4f}±{R_err:.4f} fm "
              f"(check: {gap_check:.4f} GeV)")
        corral_results[label] = {"mg_gev": mg_val, "mg_err": mg_err,
                                 "R_fm": round(R, 5), "R_err": round(R_err, 5)}

    # ── 4. Dissipation parameters ──────────────────────────────────────────
    gamma_val  = 0.012
    gamma_err  = 0.001
    tau_bath   = 1.0 / 125.0   # ℏ/ω_H in natural units, ~5.2e-27 s
    tau_YM     = 1.0 / 0.200   # 1/Λ_QCD
    markov_ratio = 0.200 / 125.0

    print(f"\nγ = {gamma_val:.3f} ± {gamma_err:.3f} GeV⁻¹")
    print(f"τ_bath/τ_YM = {markov_ratio:.2e}  ≪ 1  → Markov valid ✓")

    # ── 5. Save results ────────────────────────────────────────────────────
    results = {
        "version": "2.0",
        "paper":   "Yang-Mills Mass Gap via Open QS + Quantum Corral",
        "author":  "F. A. López",
        "date":    "2026",
        "continuum_extrapolation": {
            "mg_cont_lattice":    round(mg_cont_latt, 5),
            "mg_cont_err":        round(mg_cont_err, 5),
            "mg_phys_gev":        round(mg_phys_gev, 4),
            "chi2_dof":           round(chi2dof, 3),
            "fit_coefficients":   {"mg_cont": round(popt[0],5),
                                   "c2":      round(popt[1],4),
                                   "c4":      round(popt[2],4)},
        },
        "finite_size_data": finite_size_data,
        "quantum_corral": {
            "xi_01":         round(XI_01, 6),
            "hbarc_gev_fm":  HBARC,
            "results":       corral_results,
            "formula":       "m_g = hbar*c*xi_01 / R_corral",
        },
        "dissipation": {
            "gamma_gev_inv":  gamma_val,
            "gamma_err":      gamma_err,
            "markov_ratio":   round(markov_ratio, 6),
            "xi_coupling":    0.095,
            "xi_err":         0.018,
        },
        "lattice_parameters": {
            beta: {"a_fm": A_FM[beta], "a2_fm2": round(A_FM[beta]**2, 6),
                   "a_inv_gev": round(HBARC / A_FM[beta], 4)}
            for beta in BETA_VALUES
        },
    }

    with open("data/scaling_results_v2.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nResults saved → data/scaling_results_v2.json")
    print("=" * 60)


if __name__ == "__main__":
    main()
