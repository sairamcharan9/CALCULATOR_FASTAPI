import pytest
from decimal import Decimal
from app.operations import add, subtract, multiply, divide, nth_power, nth_root, int_divide, modulus, percent, abs_diff
from app.exceptions import DivisionByZeroError, InvalidOperationError

def test_add():
    assert add(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract():
    assert subtract(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply():
    assert multiply(Decimal('2'), Decimal('3')) == Decimal('6')

def test_divide():
    assert divide(Decimal('6'), Decimal('3')) == Decimal('2')

def test_divide_zero():
    with pytest.raises(DivisionByZeroError):
        divide(Decimal('6'), Decimal('0'))

def test_nth_power():
    assert nth_power(Decimal('2'), Decimal('3')) == Decimal('8')

def test_nth_root_normal():
    assert nth_root(Decimal('8'), Decimal('3')) == Decimal('2')

def test_nth_root_zero():
    with pytest.raises(DivisionByZeroError):
        nth_root(Decimal('8'), Decimal('0'))

def test_nth_root_negative_even():
    with pytest.raises(InvalidOperationError):
        nth_root(Decimal('-4'), Decimal('2'))

def test_int_divide():
    assert int_divide(Decimal('7'), Decimal('3')) == Decimal('2')

def test_int_divide_zero():
    with pytest.raises(DivisionByZeroError):
        int_divide(Decimal('7'), Decimal('0'))
    
def test_modulus():
    assert modulus(Decimal('7'), Decimal('3')) == Decimal('1')

def test_modulus_zero():
    with pytest.raises(DivisionByZeroError):
        modulus(Decimal('7'), Decimal('0'))

def test_percent():
    assert percent(Decimal('50'), Decimal('200')) == Decimal('25')

def test_percent_zero():
    with pytest.raises(DivisionByZeroError):
        percent(Decimal('50'), Decimal('0'))


def test_abs_diff():
    assert abs_diff(Decimal('3'), Decimal('5')) == Decimal('2')
