import pytest
from labs.lab_1.lab_1d import two_sum

def test_empty():
    assert two_sum([], 5) == []

def test_reg():
    assert two_sum([1,5,6,7,3], 4) == [0,4]
    assert two_sum([1,5,6,7,3], 7) == [0,2]
    assert two_sum([6,2,4,9,8,17], 11) == [1,3]