from filepro import  file_project
import win32api
import unittest
import os
import re
class testa(unittest.TestCase):
    def setUp(self):
        self.obj=file_project()
    def test_for_find_file(self):
        a=self.obj.find_file_in_all_drives("ProgrammingDemo.txt")
        self.assertEqual(a[0],['C:\\New folder\\ProgrammingDemo.txt',
 'C:\\New folder (2)\\ProgrammingDemo.txt'])
    def test_for_find_file1(self):
        a=self.obj.find_file_in_all_drives("ProgrammingDemo.txt")
        self.assertEqual(a[1],['E:\\chandu\\ProgrammingDemo.txt'])
