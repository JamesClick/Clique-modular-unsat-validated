# Contributing to Clique-modular-unsat-validated

Thank you for your interest in contributing to this project!

## How to Propose New Test Cases
1. Open an issue describing the SAT/UNSAT graph or formula and the desired `.cnf` file.
2. Submit a Pull Request containing:
   - The `.cnf` file in `proofs/` (for UNSAT cases, include the corresponding `.drat` proof).
   - Any scripts or data entries in `scripts/` or `data/` needed for validation.

## Running the Project Locally

```bash
# Clone the repository
git clone https://github.com/JamesClick/Clique-modular-unsat-validated.git
cd Clique-modular-unsat-validated

# (Optional) Create a Python virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# 1. Generate and validate CSV datasets
python3 scripts/fix_and_validate_tests.py

# 2. Compile the article
pdflatex main.tex && bibtex main && pdflatex main.tex
