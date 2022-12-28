import  pytest
'''def f(x):
    return x*10
def test_pytest_function():
    assert f(3) == 30
    assert f(2) == 20'''
@pytest.fixture
def numbers():
    x,y,z=10,20,30
    return [x,y,z]
def test_f1(numbers):
    a=10
    assert numbers[0]==a
@pytest.mark.skip
def test_f2(numbers):
    a="x"
    assert  numbers[1]==a
@pytest.mark.xfail
def test_f3(numbers):
    a=0
    assert numbers[1]==a