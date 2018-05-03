import unittest

import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

from pg2l.meta.grammar import MetaGrammar
from pg2l.meta.parser.parser import Parser
from pg2l.lsys.grammar import Grammar
from pg2l.lsys.generator import Generator

class TestLSysGrammar(unittest.TestCase):

    def test_lsys_grammar(self):

        M = MetaGrammar.from_declaration(
            ('START', 'S'),
            ('LETTER', list('ABCDEF')),
            ('NUMBER', range(4)),
            ('LBR', '['),
            ('RBR', ']'),
            ('REWRITE', ':'),
            ('expression', 'string'),
            ('expression', 'production'),
            ('expression', 'grammar'),
            ('string', 'symbol', 'string'),
            ('string', 'level', 'string'),
            ('string', 'empty'),
            ('symbol', 'LETTER', 'jump'),
            ('jump', 'jump', 'NUMBER'),
            ('jump', 'empty'),
            ('level', 'LBR', 'substring', 'RBR', 'jump'),
            ('substring', 'substring', 'symbol'),
            ('substring', 'empty'),
            ('grammar', 'axiom', 'NEWLINE', 'productions'),
            ('productions', 'production', 'NEWLINE', 'productions'),
            ('productions', 'empty'),
            ('axiom', 'START', 'REWRITE', 'string'),
            ('production', 'symbol', 'REWRITE', 'string'),
            )

        d = to_agraph(M)
        d.layout('dot')
        d.draw('parser.png')

        L = Grammar.from_string(M,
                                    """S:A
A:AB
B:A
"""
                                    )

        gen = Generator(L)

        # language = []
        # for sentence in Generator(L):
        #     print(sentence)
        #     language.append(sentence)

if __name__ == '__main__':
    unittest.main(verbosity=2)
