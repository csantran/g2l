# -*- coding : utf-8 -*-
import unittest

from pg2l.ast.base import AbstractSymbol
from pg2l.ast.base import AbstractNonTerminalLeafSymbol, AbstractTerminalSymbol
from pg2l.ast.base import MetaSymbol
from pg2l.ast.terminals import Constant
class TestAbstractSymbol(unittest.TestCase):

    def test_abstract_nonterminal_symbol(self):
        class Leaf(AbstractNonTerminalLeafSymbol):
            _string = None

            def __init__(self, string):
                super().__init__(string)
                self._string = string

            def __str__(self):
                return self._string

        class Char(Constant, metaclass=MetaSymbol):
            _string = None

            def __init__(self, string):
                self._string = string

            def __str__(self):
                return self._string


        class Letter(Leaf, metaclass=MetaSymbol):
            pass

        class Number(Leaf, metaclass=MetaSymbol):
            pass


        self.assertEqual(Char.symbol, 'CHAR')
        self.assertEqual(Letter.symbol, 'letter')
        self.assertEqual(Number.symbol, 'number')
        c = Char('A')
        l = Letter('B')
        n = Number('1')
        self.assertEqual(str(c), 'A')
        self.assertEqual(str(l), 'B')
        self.assertEqual(str(n), '1')
        self.assertEqual(str(repr(l)), '(letter B)')
        self.assertEqual(str(repr(c)), '(CHAR A)')
        self.assertEqual(str(repr(n)), '(number 1)')

        for x in (c,l,n):
            self.assertIsInstance(x, AbstractSymbol)

if __name__ == '__main__':
    unittest.main(verbosity=2)
