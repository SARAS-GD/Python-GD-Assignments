"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../python part 2')))
import pytest
import os
from task_read_write import extract_values_and_write

def test_extract_values_and_write(tmpdir):
    
    file1 = tmpdir.join('file_1.txt')
    file1.write('23')
    file2 = tmpdir.join('file_2.txt')
    file2.write('78')
    file3 = tmpdir.join('file_3.txt')
    file3.write('3')

    output_file = tmpdir.join('result.txt')

    extract_values_and_write(tmpdir, output_file)

    with open(output_file, 'r') as result:
        content = result.read()
    assert content == '23, 78, 3'

def test_extract_values_empty_directory(tmpdir):
    output_file = tmpdir.join('result.txt')

    extract_values_and_write(tmpdir, output_file)

    with open(output_file, 'r') as result:
        content = result.read()
    assert content == ''

def test_extract_values_with_empty_files(tmpdir):
    file1 = tmpdir.join('file_1.txt')
    file1.write('23')
    file2 = tmpdir.join('file_2.txt')
    file2.write('')  
    file3 = tmpdir.join('file_3.txt')
    file3.write('3')

    output_file = tmpdir.join('result.txt')

    extract_values_and_write(tmpdir, output_file)

    with open(output_file, 'r') as result:
        content = result.read()
    assert content == '23, 3'
