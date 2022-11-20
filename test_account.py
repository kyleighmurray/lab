import pytest
from account import *

def test_init():
    t1 = Account('ex')

    assert t1.get_balance() == 0
    assert t1.get_name() == 'ex'

def test_deposit():
    t1 = Account('ex')
    assert t1.deposit(100) is True
    assert t1.get_balance() == 100
    assert t1.deposit(.1) is True
    assert t1.get_balance() == pytest.approx(100.1, abs=0.001)
    assert t1.deposit(0) is False
    assert t1.get_balance() == pytest.approx(100.1, abs=0.001)
    assert t1.deposit(-8) is False
    assert t1.get_balance() == pytest.approx(100.1, abs=0.001)

def test_withdraw():
    t1 = Account('ex')
    t1.deposit(100.5)

    assert t1.withdraw(100) is True
    assert t1.get_balance() == pytest.approx(0.5, abs=0.001)
    assert t1.withdraw(100) is False
    assert t1.get_balance() == pytest.approx(0.5, abs=0.001)
    assert t1.withdraw(.1) is True
    assert t1.get_balance() == pytest.approx(0.4, abs=0.001)
    assert t1.withdraw(0) is False
    assert t1.get_balance() == pytest.approx(0.4, abs=0.001)
    assert t1.withdraw(-1) is False
    assert t1.get_balance() == pytest.approx(0.4, abs=0.001)
    assert t1.withdraw(-2.2) is False
    assert t1.get_balance() == pytest.approx(0.4, abs=0.001)

def test_get_balance():
    t1 = Account('ex')
    assert t1.get_balance() == 0
    t1.deposit(3)
    assert t1.get_balance() == 3
    t1.deposit(.4)
    assert t1.get_balance() == pytest.approx(3.4, abs=0.001)

def test_get_name():
    t1 = Account('John Doe')
    t2 = Account('@#%$@^')
    t3 = Account('0')

    assert t1.get_name() == 'John Doe'
    assert t2.get_name() == '@#%$@^'
    assert t3.get_name() == '0'
