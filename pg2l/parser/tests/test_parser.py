import unittest
import re
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
import ply.lex as lex
import ply.yacc as yacc

from pg2l.grammar import build, Grammar
from pg2l.parser.parser import Parser


class TestParser(unittest.TestCase):

    def test_parser(self):

        M = build(
            ('LETTER', list('ABCDEF')),
            ('NUMBER', range(4)),
            ('LBR', '['),
            ('RBR', ']'),
            ('string', 'string', 'symbol'),
            ('string', 'string', 'level'),
            ('string', 'empty'),
            ('symbol', 'LETTER', 'jump'),
            ('jump', 'jump', 'NUMBER'),
            ('jump', 'empty'),
            ('level', 'LBR', 'substring', 'RBR', 'jump'),
            ('substring', 'substring', 'symbol'),
            ('substring', 'empty'),
            )

        d = to_agraph(M)
        d.layout('dot')
        d.draw('parser.png')

        # parser = Parser(M)
        # print(parser.__dict__)
        # # yacc.yacc(module=parser, start=M.axiom)
        parser = Parser(M)
        print()
        print(repr(parser.parse('AB12[CDA]')))
        print()
        
        print(str(parser.parse('AB12[CDA]')))
        
            

if __name__ == '__main__':
    unittest.main(verbosity=2)
