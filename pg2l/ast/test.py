import unittest

from pg2l.ast.base import Leaf, KTree, BTree, BTreeLeft, BTreeRight, shallow_copy

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
        a = shallow_copy(a)
        b = shallow_copy(b)

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

        a = A(symbol='A')
        b = B(jump=1)

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

        a = shallow_copy(a)
        b = shallow_copy(b)

        root.push(b)
        self.assertEqual(root.right, b)
        self.assertIsNone(root.left)

        root.push(a)
        self.assertEqual(root.left, a)
        self.assertEqual(root.right, b)

        self.assertEqual(repr(root), '(BTREE {\'symbol\': \'A\'}{\'jump\': 1})')

if __name__ == '__main__':
    unittest.main(verbosity=2)
