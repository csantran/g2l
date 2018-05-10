import unittest


# import networkx as nx
# from networkx.drawing.nx_agraph import to_agraph

from pg2l.meta.grammar import MetaGrammar
from pg2l.meta.parser.parser import Parser
from pg2l.lsys.asg import apt_to_asg

class TestAsg(unittest.TestCase):

    def setUp(self):
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
            ('substring', 'substring', 'level'),
            ('substring', 'empty'),
            ('grammar', 'axiom', 'NEWLINE', 'productions'),
            ('productions', 'production', 'NEWLINE', 'productions'),
            ('productions', 'empty'),
            ('axiom', 'START', 'REWRITE', 'string'),
            ('production', 'symbol', 'REWRITE', 'string'),
            )

        self.parser = Parser(M)

    def test_asg_1(self):
        apt = self.parser.parse("A[B1[A[C1F]]D]E")
        S = apt_to_asg(apt)

        # d = to_agraph(S)
        # d.layout('dot')
        # d.draw('asg.png')


if __name__ == '__main__':
    unittest.main(verbosity=2)
