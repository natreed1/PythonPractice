from calculatorV2 import calculate 

def test_stringAddition():
    assert calculate("5 + 3") == 8.0
    assert calculate("( 3 + 5 + 2 ) + 5 ") == 15.0

def test_multiplaction():
    assert calculate("10 * 5") == 50.0
    assert calculate("( 2 * 3 ) * 4") == 24.0
    assert calculate("5 * 3 * ( 2 * 1 * 8 )") == 240.0

def test_subtraction():
    assert calculate("6 - 2") == 4.0
    assert calculate("( 10 - 3 ) - 2") == 5.0

def test_division():
    assert calculate("6 / 3") == 2.0
    assert calculate("( 10 / 2 ) / 5") == 1.0

def test_parentheses():
    assert calculate("( ( 2 + 5) * 3 ) / 3") == 7.0
    assert calculate("(1 + 3) * (2 + 4)") == 24.0



