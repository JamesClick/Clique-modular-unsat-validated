# Modular Clique UNSAT – Validated Data and Proofs

This repository contains only the **validated, audited, and filtered results** of the Modular Clique UNSAT project.

---

## Directory Structure

- `datasets/`: Clean `.csv` files with residues, execution time, and SAT/UNSAT status
- `graphs/`: Graphs and plots showing the modular behavior (S(φ) = 0 or ≠ 0)
- `proofs/`: Only `.drat` proofs with their corresponding `.cnf` files
- `docs/`: Formal proof (PDF), research summary, and supporting documents

---

## Validation Criteria

The following filters were applied to all data:

- No instance where `k_clique > n_vertices`
- No `time_to_unsat = 0.0` with `n_vertices > 50`
- Only modular residues consistent with the conjecture:
  - For UNSAT formulas: **S(φ) = 0** for all weights and moduli
  - For SAT formulas: **S(φ) ≠ 0** in at least one case

---

## Project Status

This repository represents the **clean and final version** of the project, ready for:

- Scientific publication
- Peer review
- Submission to conferences or journals

---

**Author:** Jamesson Richard Campos Santos da Graça  
**GitHub:** [JamesClick](https://github.com/JamesClick)
