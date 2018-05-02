import unittest

import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

from pg2l.meta.grammar import MetaGrammar
from pg2l.meta.parser.parser import Parser
from pg2l.lsys.grammar import Grammar


class TestLSysGrammar(unittest.TestCase):

    def test_lsys_grammar(self):

        M = MetaGrammar.from_declaration(
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
            ('axiom', 'string'),
            ('production', 'symbol', 'REWRITE', 'string'),
            )

        d = to_agraph(M)
        d.layout('dot')
        d.draw('parser.png')

        parser = Parser(M)

        exp = parser.parse("""A
A:AB
""")

        print(repr(exp))
        # print(repr(exp))



if __name__ == '__main__':
    unittest.main(verbosity=2)
