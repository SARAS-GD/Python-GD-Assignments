"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import pytest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../python part 2')))
from task_input_output import read_numbers

def test_read_numbers_without_text_input():
    
    with patch('builtins.input', side_effect=["1", "2", "3", "4"]):
        result = read_numbers(4)
        assert result == "Avg: 2.50"

def test_read_numbers_with_text_input():
    
    with patch('builtins.input', side_effect=["1", "2", "hello", "4"]):
        result = read_numbers(4)
        assert result == "Avg: 2.33"

def test_read_numbers_all_text():
    
    with patch('builtins.input', side_effect=["hello", "world", "foo", "bar"]):
        result = read_numbers(4)
        assert result == "No numbers entered"

def test_read_numbers_mixed_input():
    
    with patch('builtins.input', side_effect=["10", "invalid", "20", "30"]):
        result = read_numbers(4)
        assert result == "Avg: 20.00"
