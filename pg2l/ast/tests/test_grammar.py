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
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import tempfile
import tkinter as tk

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

        print('#')
        print(meta.axiom)
        print(meta.terminals)
        print(meta.nonterminals)
        print(meta.productions)
        # A = to_agraph(meta.derivation_graph)
        # A.layout('dot')
        # A.draw('multi.png')

        print(meta.derivation_graph.edges(data=True))
        print(list(nx.selfloop_edges(meta.derivation_graph)))
        
        # pos = nx.spring_layout(meta.derivation_graph)
        # nx.draw_networkx_nodes(meta.derivation_graph, pos)
        # nx.draw_networkx_labels(meta.derivation_graph, pos)
        # nx.draw_networkx_edges(meta.derivation_graph, pos)
        # plt.show()

        # toPdot = nx.drawing.nx_pydot.to_pydot
        # pdot = toPdot(meta.derivation_graph)
        # # plt = Image.open().show()

        # root = tk.Tk()
        # image = tk.PhotoImage(pdot.create_png())
        # label = tk.Label(image=image)
        # label.pack()
        # root.mainloop()
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
