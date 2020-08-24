import unittest
from dataclasses import dataclass

from remove_dups.remove_dups import remove_duplicates


@dataclass
class TestObject:
    one: str
    two: str


class RemoveDuplicateTest(unittest.TestCase):

    def test_remove_duplicates(self):
        no_duplicates = remove_duplicates([1, 2, 2, 2, 3, 4, 5])

        self.assertListEqual(no_duplicates, [1, 2, 3, 4, 5])

    def test_remove_out_of_order(self):
        no_duplicates = remove_duplicates([5, 2, 4, 6, 2, 7, 4, 99, 5, 2, 11])

        self.assertListEqual(no_duplicates, [5, 2, 4, 6, 7, 99, 11])

    def test_remove_duplicate_strings(self):
        no_duplicates = remove_duplicates(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])

        self.assertListEqual(no_duplicates, ['one', 'fish', 'two', 'red', 'blue'])

    def test_remove_duplicate_objects(self):
        no_duplicates = remove_duplicates([
            TestObject('fish', 'fish'),
            TestObject('red', 'blue'),
            TestObject('fish', 'fish'),
            TestObject('red', 'blue'),
        ])

        self.assertListEqual(no_duplicates, [TestObject('fish', 'fish'), TestObject('red', 'blue')])
