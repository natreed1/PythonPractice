from  calculatorComp import computation  


def test_addition():
    assert computation(["+"], [2, 3]) == 5
    assert computation(["+"], [1, 1]) == 2
    assert computation(["+"], [0, 0]) == 0
    assert computation(["+"], [-1, 1]) == 0
    assert computation(["+", "+", "+"], [1, 10, 15]) == 26
def test_subtraction():
    assert computation(["-"], [5, 3]) == 2
    assert computation(["-"], [10, 5]) == 5
    assert computation(["-"], [0, 0]) == 0
    assert computation(["-"], [1, 1]) == 0
    assert computation(["-", "-", "-"], [10, 3, 2]) == 5
def test_multiplication():
    assert computation(["*"], [2, 3]) == 6
    assert computation(["*"], [1, 1]) == 1
    assert computation(["*"], [0, 5]) == 0
    assert computation(["*", "*"], [2, 3, 4]) == 24
    assert computation(["*", "*", "*"], [2, 3, 4, 5]) == 120
def test_division():
    assert computation(["/"], [10, 2]) == 5
    assert computation(["/"], [15, 3]) == 5
    assert computation(["/"], [0, 5]) == 0
    assert computation(["/", "/"], [20, 2, 2]) == 5
def test_complex():
    assert computation(["+", "*"], [1, 2, 3]) == 9
    assert computation(["*", "+"], [2, 3, 4]) == 10
    assert computation(["+", "-"], [1, 2, 3]) == 0
def test_all():
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_complex()

test_all()
