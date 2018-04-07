# -*- coding : utf-8 -*-
import unittest

from pg2l.grammar import Grammar, terminals
from pg2l.parser.terminal.base import lexer_factory


def get_tokens(lexer):
    toks = []
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        toks.append(tok)

    return [(x.type, x.value) for x in toks]

class TestLexer(unittest.TestCase):
    def test_letter(self):
        lexer = lexer_factory((terminals[Grammar.LETTER], ('ABCD',), {}),)
        lexer.lexer.input('A')

        self.assertEqual(get_tokens(lexer), [('LETTER', 'A')])

        lexer.lexer.input('Z')
        self.assertEqual(get_tokens(lexer), [])

    def test_number(self):
        lexer = lexer_factory((terminals[Grammar.NUMBER], (-1,0,1), {}),)
        lexer.lexer.input('10-1')

        self.assertEqual(get_tokens(lexer), [('NUMBER', 1), ('NUMBER', 0), ('NUMBER', -1)])

        lexer.lexer.input('2')
        self.assertEqual(get_tokens(lexer), [])

    def test_constants(self):
        lexer = lexer_factory((terminals[Grammar.LBR], ('[',), {}),)
        lexer.lexer.input('[')

        self.assertEqual(get_tokens(lexer), [('LBR', '[')])

        lexer = lexer_factory((terminals[Grammar.RBR], (']',), {}),)
        lexer.lexer.input(']')

        self.assertEqual(get_tokens(lexer), [('RBR', ']')])
        
        lexer = lexer_factory((terminals[Grammar.LBR], ('['), {}),
                              (terminals[Grammar.RBR], (']'), {}))
        
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = lexer_factory((terminals[Grammar.LBR], (), {}),
                              (terminals[Grammar.RBR], (), {}))
        
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = lexer_factory((terminals[Grammar.LBR], ('('), {}),
                              (terminals[Grammar.RBR], (')'), {}))
        
        lexer.lexer.input('()')

        self.assertEqual(get_tokens(lexer), [('LBR', '('), ('RBR', ')')])

if __name__ == '__main__':
    unittest.main(verbosity=2)
