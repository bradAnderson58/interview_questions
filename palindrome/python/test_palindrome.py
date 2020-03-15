
import unittest
from palindrome import is_palindrome

class PalindromeTest(unittest.TestCase):

    def test_palindromes(self):
        otto = 'otto'
        hannah = 'hannah'
        tacocat = 'tacocat'

        self.assertTrue(is_palindrome(otto))
        self.assertTrue(is_palindrome(hannah))
        self.assertTrue(is_palindrome(tacocat))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('notpalindrome'))
        self.assertFalse(is_palindrome('tacohat'))
        self.assertFalse(is_palindrome('otot'))
