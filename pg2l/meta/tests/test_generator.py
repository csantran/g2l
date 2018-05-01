import unittest

# import networkx as nx
# from networkx.drawing.nx_agraph import to_agraph

from pg2l.meta.grammar import MetaGrammar
from pg2l.meta.generator import SimpleGenerator


class TestParser(unittest.TestCase):

    def test_parser(self):

        M = MetaGrammar.from_declaration(
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

        # d = to_agraph(M)
        # d.layout('dot')
        # d.draw('parser.png')

        # parser = Parser(M)
        # print(parser.__dict__)
        # # yacc.yacc(module=parser, start=M.axiom)


        print(SimpleGenerator.generate(M, ['string'], 10))

        # def test_parser(self):
        #     from pg2l.grammar import MetaGrammar, Grammar
        #     from pg2l.grammar.declaration import S, empty
        #     from pg2l.meta import Parser
        #     from pg2l import Generator

        #     M = MetaGrammar.from_declarations(
        #         ('LETTER', list('ABCDEF')),
        #         ('NUMBER', range(4)),
        #         ('LBR', '['),
        #         ('RBR', ']'),
        #         ('string', 'string', 'symbol'),
        #         ('string', 'string', 'level'),
        #         ('string', 'empty'),
        #         ('symbol', 'LETTER', 'jump'),
        #         ('jump', 'jump', 'NUMBER'),
        #         ('jump', 'empty'),
        #         ('level', 'LBR', 'substring', 'RBR', 'jump'),
        #         ('substring', 'substring', 'symbol'),
        #         ('substring', 'empty'),
        #         )

        #     M = MetaGrammar.from_string(
        #         """
        #         # constants
        #         LBR -> [                         
        #         RBR -> ]                         

        #         # nonterminals
        #         string -> string symbol   [.5]
        #                 | string level    [.25]
        #                 | empty           [.25]

        #         symbol -> LETTER jump     

        #         jump -> jump NUMBER       [2/3]
        #               | empty             [1/3]

        #         level -> LBR substring RBR jump

        #         substring -> substring symbol [.75]
        #                    | empty            [.25]
        #         """
        #         )

        #     V = MetaGrammar.from_string(
        #         """
        #         # variables
        #         LETTER -> ('A', cls)|('B',func)|('C',list)
        #         NUMBER -> 0|1|2|3|4
        #         """)

        #     V = MetaGrammar.from_declaration(
        #         ('LETTER', list('ABCDEF')),
        #         ('LETTER', {
        #             'A': cls,
        #             'B': func,
        #             'C': list,
        #             }
        #             )
        #         ('NUMBER', range(5)),
        #         )

        #     M = M+V

        #     sym = M.symbol

        #     L = Grammar.from_generator(
        #         meta = M,
        #         seed = [
        #             'LETTER',
        #             sym.production,
        #             'production'
        #             ],
        #         probability = map(lambda x: (x, random()), M.nonterminals)
        #         )

        #     L = Grammar.from_generator(
        #         meta = M,
        #         seed = [sym.grammar],
        #         deep = 5
        #         )

        #     L = Grammar.from_string(M,
        #                                 """
        #                                 S : A
        #                                 A : AB
        #                                 B : A
        #                                 """
        #                                 )

        #     L = Grammar.from_declaration(M,
        #                                      (
        #                                          ('S', 'A'),
        #                                          ('A', 'AB'),
        #                                          ('B', 'A'),
        #                                      )
        #                                     )

        #     generator = Generator(M)
        #     generator.generate(seed=[M.symbol.string], 5)
        #     parser = Parser(M)

        #     generator = Generator(L)

        #     lang = generator.generate(n=10)
        #     lang = generator.generate(seed=L.axiom, n=10)
        #     lang = generator.generate(seed=parser.parse('A1B1A'), n=10, trace=True)

if __name__ == '__main__':
    unittest.main(verbosity=2)
