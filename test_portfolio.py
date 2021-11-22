from portfolio import Portfolio
from portfolio import Shares
import pytest

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy(Shares("IBM", 100, 176.48))
    assert p.cost() == 17648.0

def test_buy_two_stock():
    p = Portfolio()
    p.buy(Shares("IBM", 100, 176.48))
    p.buy(Shares("HPQ", 100, 36.15))
    assert p.cost() == 21263.0

def test_not_enough_arguments_to_buy():
    p = Portfolio()
#    try:
#        p.buy("IBM")
#    except TypeError:
#        pass
#    else:
#        assert False
    with pytest.raises(TypeError):
        p.buy(Shares("IBM"))