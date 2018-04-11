# -*- coding : utf-8 -*-
import unittest

from pg2l.ast.terminals import Letter, Number
from pg2l.ast.base import AbstractSymbol

class TestAstAst(unittest.TestCase):
    def test_terminals(self):
        self.assertEqual(Letter.name, 'LETTER')
        self.assertEqual(Number.name, 'NUMBER')
        l = Letter('R')
        n = Number('1')

        self.assertIsInstance(l, AbstractSymbol)
        self.assertEqual(str(l), 'R')
        self.assertEqual(str(n), '1')
        self.assertEqual(repr(l), '(LETTER R)')
        self.assertEqual(repr(n), '(NUMBER 1)')

if __name__ == '__main__':
    unittest.main(verbosity=2)
