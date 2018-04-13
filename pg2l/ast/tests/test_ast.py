# -*- coding : utf-8 -*-
import unittest

from pg2l.ast import ast
from pg2l.ast.base import AbstractSymbol
from pg2l.ast.base import AbstractNonTerminalLeafSymbol, AbstractNonTerminalBranchSymbol

class TestAstAst(unittest.TestCase):
    # def test_empty(self):
    #     e = ast.Empty()
    #     self.assertEqual(str(e), '')
    #     self.assertEqual(e.value, '')

    def setUp(self):
        self.l = ast.Label('A')
        self.j = ast.Jump('-1')
        self.e = ast.Empty()

    def test_nonterminal_leaf(self):
        self.assertEqual(ast.Label.symbol, 'label')
        self.assertEqual(ast.Jump.symbol, 'jump')
        self.assertEqual(ast.Empty.symbol, 'empty')

        self.assertEqual(repr(self.l), '(label A)')
        self.assertEqual(repr(self.j), '(jump -1)')
        self.assertEqual(repr(self.e), '(empty)')

        self.assertEqual(str(self.l), 'A')
        self.assertEqual(str(self.j), '-1')
        self.assertEqual(str(self.e), '')

        for x in (self.l, self.j, self.e):
            self.assertIsInstance(x, AbstractSymbol)
            self.assertIsInstance(x, AbstractNonTerminalLeafSymbol)

    def test_nonterminal(self):
        r = ast.Round()
        s = ast.JNode()
        r.push(self.j)
        s.push(self.l)
        s.push(r)

        self.assertIsInstance(r, AbstractNonTerminalBranchSymbol)
        self.assertIsInstance(s, AbstractNonTerminalBranchSymbol)
        self.assertEqual(repr(s), '(jnode A-1)')
        self.assertEqual(str(s), 'A-1')
        self.assertEqual([repr(x) for x in s], [
            '(jnode A-1)',
            '(label A)',
            '(round -1)',
            '(jump -1)'
            ])

        m = ast.JModule()
        lm = ast.Level()
        lm.push(s)
        m.push(lm)

        with self.assertRaises(AssertionError):
            m.push(r)

        m.push(ast.copy(r))
        self.assertEqual(repr(m), '(jmodule [A-1]-1)')
        self.assertEqual(str(m), '[A-1]-1')
if __name__ == '__main__':
    unittest.main(verbosity=2)
