# -*- coding : utf-8 -*-
import unittest

from pg2l.ast.base import AbstractTerminalSymbol
from pg2l.ast.base import MetaSymbol
from pg2l.ast import Grammar as G


class TestGrammar(unittest.TestCase):

    def test_terminal_leaf(self):
        class Op_Rewrite(AbstractTerminalSymbol, metaclass=MetaSymbol):
            pass

        self.assertEqual(Op_Rewrite.name, 'OP_REWRITE')
        self.assertEqual(G.OP_REWRITE, Op_Rewrite)

if __name__ == '__main__':
    unittest.main(verbosity=2)
