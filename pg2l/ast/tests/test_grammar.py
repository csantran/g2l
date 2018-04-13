# -*- coding : utf-8 -*-
import unittest

# from pg2l.ast.base import AbstractTerminalSymbol
# from pg2l.ast.base import MetaSymbol
from pg2l.ast import MetaDeclaration as G, MetaGrammar


# class TestMetaDeclaration(unittest.TestCase):

#     def test_terminal_leaf(self):
#         class Op_Rewrite(AbstractTerminalSymbol, metaclass=MetaSymbol):
#             pass

#         self.assertEqual(Op_Rewrite.name, 'OP_REWRITE')
#         self.assertEqual(G.OP_REWRITE, Op_Rewrite)

class TestMetaGrammar(unittest.TestCase):

    def test_meta_grammar(self):
        meta = MetaGrammar(
            G.expression,
            (G.LETTER, 'AB'),
            (G.NUMBER, (1,)),
            (G.LBR, '['),
            (G.RBR, ']'),
            (G.REWRITE, ':'),
            (G.expression, G.axiom),
            (G.axiom, G.level),
            (G.level, G.basenode),
            (G.level, G.level, G.basenode),
            (G.basenode, G.node),
            (G.node, G.label),
            (G.label, G.LETTER),
            )

        
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
