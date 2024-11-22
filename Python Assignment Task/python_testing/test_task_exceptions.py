"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""


import typing
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../python part 2')))
from task_exceptions import division, DivisionByOneException

def test_division_ok(capfd):
    result = division(4, 2)
    out, _ = capfd.readouterr()
    assert result == 2
    assert out == "2\nDivision finished\n"  

def test_division_by_zero(capfd):
    result = division(1, 0)
    out, _ = capfd.readouterr()
    assert result is None
    assert out == "Division by 0\nDivision finished\n"

def test_division_by_one(capfd):
    with pytest.raises(DivisionByOneException) as exc_info:
        division(1, 1)
    
    assert str(exc_info.value) == "Deletion on 1 gets the same result"
    
    out, _ = capfd.readouterr()
    assert out == ""
