# -*- coding : utf-8 -*-
from collections import defaultdict
from functools import reduce
import unittest

import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

from pg2l.grammar.grammar import build, Grammar

class TestMetaGrammar(unittest.TestCase):

    def test_meta_grammar(self):

        M = build( 
            ('S', 'F'),
            ('S', '(', 'S', '+', 'F', ')'),
            ('F', '1'),
            )

        print()
        print('AX', M.axiom)
        print('TERM', M.terminals)
        print('NTERM', M.nonterminals)
        print('PRODS', list(M.productions))
        print('ALPHA', M.alphabet)
        
        d = to_agraph(M.graph)
        d.layout('dot')
        d.draw('meta.png')

if __name__ == '__main__':
    unittest.main(verbosity=2)
