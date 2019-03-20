
import unittest
from recursive_middle import Node, Linked, find_recursive_middle

class RecursiveMiddleTest(unittest.TestCase):

    def test_1(self):
        linked = create_linked(9)

        middle_val = find_recursive_middle(linked)

        self.assertEqual(middle_val, 5)


    def test_2(self):
        linked = create_linked(10)

        middle_val = find_recursive_middle(linked)

        self.assertEqual(middle_val, 6)

    def test_3(self):
        linked = create_linked(1)

        middle_val = find_recursive_middle(linked)

        self.assertEqual(middle_val, 1)

    def test_4(self):
        linked = Linked()

        middle_val = find_recursive_middle(linked)

        self.assertIsNone(middle_val)

    
def create_linked(num_nodes: int) -> Linked[int]:
    linked = Linked()
    for ind in range(1, num_nodes+1):
        linked.append(ind)

    return linked
