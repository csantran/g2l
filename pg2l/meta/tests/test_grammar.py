# -*- coding : utf-8 -*-
import unittest

# from pg2l.ast.base import AbstractTerminalSymbol
# from pg2l.ast.base import MetaSymbol
from pg2l.meta.grammar import MetaGrammar
# from pg2l.meta.declaration import MetaDeclaration as G

# class TestMetaDeclaration(unittest.TestCase):

#     def test_terminal_leaf(self):
#         class Op_Rewrite(AbstractTerminalSymbol, metaclass=MetaSymbol):
#             pass

#         self.assertEqual(Op_Rewrite.name, 'OP_REWRITE')
#         self.assertEqual(G.OP_REWRITE, Op_Rewrite)
import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
# import tempfile
# import tkinter as tk

from pg2l.meta import declaration as G

class TestMetaGrammar(unittest.TestCase):

    def test_meta_grammar(self):
        meta = MetaGrammar(
            ('LETTER', 'AB', G.VAR),
            ('NUMBER', [0,1,2], G.VAR),
            # ('LBR', '[', G.CONST),
            # ('RBR', ']', G.CONST),
            # ('REWRITE', ':', G.CONST),
            (G.S, 'expression'),
            ('expression', 'axiom'),
            ('axiom', 'level'),
            ('level', 'basenode'),
            ('level', 'level', 'basenode'),
            ('basenode', 'node'),
            ('basenode', 'jnode'),
            ('node', 'label'),
            ('label', 'LETTER'),
            ('jnode', 'node', 'round'),
            ('round', 'number'),
            ('round', 'round', 'number'),
            ('number', 'NUMBER'),
            )

        print('#')
        print(meta)
        # print(meta.axiom)
        # print(meta.terminals)
        # print(meta.nonterminals)
        # print(meta.productions)
        A = to_agraph(meta.derivation_graph)
        A.layout('dot')
        A.draw('multi.png')
        
        # print(meta.derivation_graph.edges(data=True))
        # print(list(nx.selfloop_edges(meta.derivation_graph)))

if __name__ == '__main__':
    unittest.main(verbosity=2)
