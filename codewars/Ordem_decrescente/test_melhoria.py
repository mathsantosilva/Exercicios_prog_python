import pytest
from codewars.Ordem_decrescente.Melhoria import descending_order


def test_descending_order():
    assert descending_order(0) == 0
    assert descending_order(15) == 51
    assert descending_order(123456789) == 987654321
