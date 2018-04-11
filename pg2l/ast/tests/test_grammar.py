# -*- coding : utf-8 -*-
import unittest

from pg2l.ast.base import AbstractTerminalSymbol
from pg2l.ast.base import MetaSymbol
from pg2l.ast import Grammar as G


class TestGrammar(unittest.TestCase):

    def test_terminal_leaf(self):
        class Op_Rewrite(AbstractTerminalSymbol, metaclass=MetaSymbol):
            pass

        print(Op_Rewrite.name)
        print(G.OP_REWRITE)
if __name__ == '__main__':
    unittest.main(verbosity=2)
