import pytest
@pytest.mark.parametrize("a,b,c",[(1,2,3),(7,8,9)])
def test_(a,b,c):
    assert a+b==c