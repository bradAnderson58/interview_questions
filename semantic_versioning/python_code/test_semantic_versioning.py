# python -m unittest test_semantic_versioning.py 
import unittest
from semantic_versioning import SemanticVersionQuestion, SemanticVersionException


class SemanticVersionTest(unittest.TestCase):

    def test_1(self):
        arg1 = '1.1.0'
        arg2 = '1.2.0'
        self.assertEqual(arg2, SemanticVersionQuestion.get_greater_version(arg1, arg2))

    def test_2(self):
        arg1 = '1.2.0'
        arg2 = '1.2.0'
        self.assertEqual(arg1, SemanticVersionQuestion.get_greater_version(arg1, arg2))

    def test_3(self):
        arg1 = '1.a.0'
        arg2 = '1.2.0'
        with self.assertRaises(SemanticVersionException) as cm:
            SemanticVersionQuestion.get_greater_version(arg1, arg2)

        self.assertEqual(cm.exception.message, 'Invalid Format: Non-numeric values detected')

    def test_4(self):
        arg1 = ''
        arg2 = '1.2.0'
        with self.assertRaises(SemanticVersionException) as cm:
            SemanticVersionQuestion.get_greater_version(arg1, arg2)

        self.assertEqual(cm.exception.message, 'Invalid Format: Values must take the form X.Y.Z')

    def test_5(self):
        arg1 = None
        arg2 = '1.2.0'
        with self.assertRaises(SemanticVersionException) as cm:
            SemanticVersionQuestion.get_greater_version(arg1, arg2)

        self.assertEqual(cm.exception.message, 'Invalid Format: Null value detected')

    def test_6(self):
        arg1 = '1.2.3.4.5.6'
        arg2 = '1.2.0'
        with self.assertRaises(SemanticVersionException) as cm:
            SemanticVersionQuestion.get_greater_version(arg1, arg2)

        self.assertEqual(cm.exception.message, 'Invalid Format: Values must take the form X.Y.Z')

    def test_7(self):
        arg1 = '1..6'
        arg2 = '1.2.0'
        with self.assertRaises(SemanticVersionException) as cm:
            SemanticVersionQuestion.get_greater_version(arg1, arg2)

        self.assertEqual(cm.exception.message, 'Invalid Format: Values must take the form X.Y.Z')

    def test_8(self):
        arg1 = '1.6'
        arg2 = '1.2.0'
        with self.assertRaises(SemanticVersionException) as cm:
            SemanticVersionQuestion.get_greater_version(arg1, arg2)

        self.assertEqual(cm.exception.message, 'Invalid Format: Values must take the form X.Y.Z')
