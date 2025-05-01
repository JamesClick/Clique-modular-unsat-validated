# Clique-modular-unsat-validated

Modular Residue Method for UNSAT Detection: A Restricted Conjecture for Linear Boolean Formulas.

## Repository Structure

. ├── main.tex              # LaTeX source for the article ├── refs.bib              # Bibliography database ├── LICENSE               # MIT License ├── README.md             # Project overview and quick start ├── datasets/             # Validated CSV datasets │   ├── .gitkeep │   └── ... ├── data/                 # Final CSV outputs from validation │   └── ... ├── proofs/               # CNF formulas and DRAT proofs │   ├── .gitkeep │   └── ... ├── docs/                 # Generated PDF, supplementary materials │   ├── .gitkeep │   └── ... ├── scripts/              # Validation and plotting scripts │   ├── .gitkeep │   └── fix_and_validate_tests.py ├── figures/              # Generated plot images (PDF/PNG) │   └── ... └── .github/              # CI configuration └── workflows/ └── ci.yml

## Quick Start

```bash
git clone https://github.com/JamesClick/Clique-modular-unsat-validated.git
cd Clique-modular-unsat-validated

# 1. Generate and validate datasets
python3 scripts/fix_and_validate_tests.py

# 2. Compile the article
pdflatex main.tex && bibtex main && pdflatex main.tex
