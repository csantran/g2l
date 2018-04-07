import unittest

from pg2l.ast.base import Leaf, KTree, BTree, BTreeLeft, BTreeRight
from pg2l.ast.ast import copy

class TestAstBase(unittest.TestCase):
    def test_bynary_tree_kt_kt(self):
        class A(KTree, BTreeLeft):
            pass

        class B(KTree, BTreeRight):
            pass

        a = A()
        b = B()

        root = BTree()
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

        root.push(a)
        self.assertEqual(root.left, a)
        self.assertIsNone(root.right)

        root.push(b)
        self.assertEqual(root.left, a)
        self.assertEqual(root.right, b)

        root = BTree()
        a = copy(a)
        b = copy(b)

        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

        root.push(b)
        self.assertEqual(root.right, b)
        self.assertIsNone(root.left)

        root.push(a)
        self.assertEqual(root.left, a)
        self.assertEqual(root.right, b)

    def test_bynary_tree_leaf_leaf(self):
        class A(Leaf, BTreeLeft):
            pass

        class B(Leaf, BTreeRight):
            pass

        a = A()
        b = B()

        root = BTree()
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

        root.push(a)
        self.assertEqual(root.left, a)
        self.assertIsNone(root.right)

        root.push(b)
        self.assertEqual(root.left, a)
        self.assertEqual(root.right, b)

        root = BTree()
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

        a = copy(a)
        b = copy(b)

        root.push(b)
        self.assertEqual(root.right, b)
        self.assertIsNone(root.left)

        root.push(a)
        self.assertEqual(root.left, a)
        self.assertEqual(root.right, b)

if __name__ == '__main__':
    unittest.main(verbosity=2)
