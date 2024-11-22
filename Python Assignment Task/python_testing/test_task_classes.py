"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import sys
import os
import unittest
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../python part 2')))
from task_classes import Homework, Student, Teacher

class TestHomework(unittest.TestCase):
    def test_homework_creation(self):
        hw = Homework('Task 1', 3)
        self.assertEqual(hw.text, 'Task 1')
        self.assertTrue(isinstance(hw.created, datetime.datetime))
        self.assertTrue(isinstance(hw.deadline, datetime.timedelta))
        self.assertEqual(hw.deadline, datetime.timedelta(days=3)) 

    def test_is_active(self):
        hw = Homework('Active task', 5)
        self.assertTrue(hw.is_active())
        expired_hw = Homework('Expired task', -1)  
        self.assertFalse(expired_hw.is_active())

class TestStudent(unittest.TestCase):
    def test_do_homework_active(self):
        hw = Homework('Active task', 5)
        student = Student('Vladislav', 'Popov')
        self.assertEqual(student.do_homework(hw), hw)

    def test_do_homework_expired(self):
        expired_hw = Homework('Expired task', 0) 
        student = Student('Vladislav', 'Popov')
        self.assertIsNone(student.do_homework(expired_hw))

class TestTeacher(unittest.TestCase):
    def test_create_homework(self):
        teacher = Teacher('Dmitry', 'Orlyakov')  
        hw = teacher.create_homework('New task', 7)
        self.assertEqual(hw.text, 'New task')
        self.assertEqual(hw.deadline, datetime.timedelta(days=7))  

    def test_create_homework_negative_days(self):
        teacher = Teacher('Dmitry', 'Orlyakov') 
        hw = teacher.create_homework('Impossible task', -5)
        self.assertEqual(hw.text, 'Impossible task')
        self.assertFalse(hw.is_active())

if __name__ == '__main__':
    unittest.main()
