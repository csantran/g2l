# -*- coding : utf-8 -*-
import unittest

from pg2l.grammar import Grammar, lexers
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
        print(Grammar.LETTER)
        print(lexers)

        lexer = lexer_factory((lexers[Grammar.LETTER], ('ABCD',), {}),)
        lexer.lexer.input('A')

        self.assertEqual(get_tokens(lexer), [('LETTER', 'A')])

        lexer.lexer.input('Z')
        self.assertEqual(get_tokens(lexer), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
