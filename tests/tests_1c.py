import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_empty_list():
    assert max_subarray_sum([]) == None

def test_standard_case():
    assert max_subarray_sum([2,4,-3,18,17,24,-30,39]) == 73