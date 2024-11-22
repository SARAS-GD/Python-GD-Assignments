"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../python part 2')))

from task_read_write_2 import generate_words, write_files

@pytest.fixture
def generated_words():
    return generate_words(20)

def test_generate_words(generated_words):
    assert len(generated_words) == 20
    for word in generated_words:
        assert 3 <= len(word) <= 10
        assert word.isalpha()

def test_write_files(generated_words, tmp_path):
    file1_path = tmp_path / 'file_task_4_1.txt'
    file2_path = tmp_path / 'file_task_4_2.txt'
    
    write_files(generated_words)
    
    os.rename('file_task_4_1.txt', file1_path)
    os.rename('file_task_4_2.txt', file2_path)
    
    with open(file1_path, 'r', encoding='utf-8') as f:
        file1_content = f.read().splitlines()
        assert file1_content == generated_words
    
    reversed_words = generated_words[::-1]
    with open(file2_path, 'r', encoding='cp1252') as f:
        file2_content = f.read()
        assert file2_content == ','.join(reversed_words)

