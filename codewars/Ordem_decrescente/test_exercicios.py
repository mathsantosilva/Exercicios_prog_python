import pytest
from codewars.Ordem_decrescente.Exercicios import encontrar_extremos, mover_zeros, ordenar_e_contar, segundo_maior
# EXERCÍCIO 1 — MAIOR E MENOR

@pytest.mark.parametrize("numeros, esperado", [
    ([4, 9, 2, 7, 1], (9, 1)),
    ([10, 10, 5, 3], (10, 3)),
    ([-5, -2, -8, -1], (-1, -8)),
    ([7], (7, 7)),
    ([0, 0, 0], (0, 0)),
    ([-10, 0, 10], (10, -10)),
    ([], (None)),
])
def test_encontrar_extremos(numeros, esperado):
    assert encontrar_extremos(numeros) == esperado


# EXERCÍCIO 2 — MOVER ZEROS

@pytest.mark.parametrize("numeros, esperado", [
    ([0, 3, 0, 5, 2], [3, 5, 2, 0, 0]),
    ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 1], [1, 0]),
    ([1, 0], [1, 0]),
    ([-1, 0, -2, 0, 3], [-1, -2, 3, 0, 0]),
    ([], []),
])
def test_mover_zeros(numeros, esperado):
    assert mover_zeros(numeros) == esperado


# EXERCÍCIO 3 — BUBBLE SORT + CONTAGEM

@pytest.mark.parametrize("numeros, esperado", [
    ([3, 2, 1], ([1, 2, 3], 3)),
    ([1, 2, 3], ([1, 2, 3], 0)),
    ([2, 1, 3], ([1, 2, 3], 1)),
    ([5, 4, 3, 2, 1], ([1, 2, 3, 4, 5], 10)),
    ([3, 1, 2], ([1, 2, 3], 2)),
    ([2, 2, 1], ([1, 2, 2], 2)),
    ([-1, -3, -2], ([-3, -2, -1], 2)),
    ([7], ([7], 0)),
    ([], ([], 0)),
])
def test_ordenar_e_contar(numeros, esperado):
    assert ordenar_e_contar(numeros) == esperado


# EXERCÍCIO 4 — SEGUNDO MAIOR DISTINTO

@pytest.mark.parametrize("numeros, esperado", [
    ([4, 8, 2, 9, 5], 8),
    ([10, 10, 8, 6], 8),
    ([3, 3, 3], None),
    ([-5, -1, -3], -3),
    ([1, 2], 1),
    ([2, 1], 1),
    ([5, 5, 4, 4], 4),
    ([0, -1, -2], -1),
    ([10], None),
    ([], None),
])
def test_segundo_maior(numeros, esperado):
    assert segundo_maior(numeros) == esperado
