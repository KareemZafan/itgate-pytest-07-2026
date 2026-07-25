from src import calculator as calc
import pytest
from datetime import datetime

add_test_data= [(2,3,5),(-1,1,0),(1,-100,-99),(90,-80,10),(-90,90,0),(0,-90,-90),(100,1000,1100)]


@pytest.mark.APRIL_RELEASE
@pytest.mark.parametrize("a,b,sum",add_test_data)
def test_add(a,b,sum):
    assert calc.add(a,b) == sum


## Code duplication with different test data for sum function
@pytest.mark.parametrize("a,b,acc",add_test_data)
def test_sum(a,b,acc):
    assert calc.sum(a,b) == acc
    

def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -100) == 99
    assert calc.subtract(90, -80) == 170
    assert calc.subtract(-90, 90) == -180
    assert calc.subtract(0, -90) == 90


mul_test_data= [(2,3,6),(-1,0,0),(1,-100,-100),(90,-80,-7200),(-90,90,-8100),(0,-90,0),(100,10,1000)]
@pytest.mark.parametrize("a,b,product",mul_test_data)
def test_multiply(a,b,product):
    assert calc.multiply(a,b) == product

@pytest.mark.Integration
def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-100, -10) == 10
    assert calc.divide(90, -9) == -10
    assert calc.divide(-90, 9) == -10
    with pytest.raises(ValueError):
        calc.divide(5, 0)

#@pytest.mark.xfail(reason="This test is expected to fail due to known issue with power function")
def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(-1, 1) == -1
    assert calc.power(-2, 2) == 4
    assert calc.power(9, -2) == 1/81
    assert calc.power(-3, 0) == 1

@pytest.mark.Integration
def test_sqrt():
    assert calc.sqrt(4) == 2
    assert calc.sqrt(0) == 0
    assert calc.sqrt(169) == 13
    with pytest.raises(ValueError):
        calc.sqrt(-1)  

#@pytest.mark.skip(reason="Not implemented yet")
def test_abs():
    assert calc.abs(-5) == 5
    assert calc.abs(0) == 0
    assert calc.abs(100) == 100

@pytest.mark.APRIL_RELEASE
@pytest.mark.Integration
def test_mod():
    assert calc.mod(12, 5) == 2
    assert calc.mod(21, 8) == 5
    assert calc.mod(5, -3) == -1
    with pytest.raises(ValueError):
        calc.mod(5, 0)

day = 29
# day = datetime.now().day

@pytest.mark.skipif(day < 28, reason="You can only run this test after 28th of the month")
def test_bill_payment_message():
    ## This is a test case for the bill payment message, consider the code to test the message sending
    assert 100 > 0


def test_factorial():
    assert calc.factorial(0) == 0
    assert calc.factorial(1) == 1
    assert calc.factorial(5) == 120
    with pytest.raises(ValueError):
        calc.factorial(-1)