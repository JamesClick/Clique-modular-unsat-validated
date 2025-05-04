import pytest
from scripts.fix_and_validate_tests import calculate_mod_sum
from scripts.fix_and_validate_tests import load_formula

# Test if mod_sum is zero for known UNSAT formula
def test_mod_sum_zero_for_known_unsat():
    # Carregar uma fórmula conhecida de 3-SAT UNSAT
    formula = load_formula("proofs/random_3sat_unsat_n20_c86.cnf")
    # Verificar se a soma ponderada modular é igual a 0 (conjectura válida)
    assert calculate_mod_sum(formula) == 0

# Test if mod_sum is non-zero for known SAT formula
def test_mod_sum_non_zero_for_known_sat():
    # Carregar uma fórmula conhecida de 3-SAT SAT
    formula = load_formula("proofs/random_3sat_unsat_n22_c90.cnf")
    # Verificar se a soma ponderada modular não é igual a 0 (conjectura não válida)
    assert calculate_mod_sum(formula) != 0
