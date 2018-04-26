import unittest

import ply.lex as lex

from pg2l.grammar import build
from pg2l.parser.lexer import Lexer


def get_tokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break

        yield tok.type, tok.value

class TestLexer(unittest.TestCase):

    def test_lexer(self):

        M = build(
            ('LETTER', list('ABCDEF')),
            ('NUMBER', range(4)),
            ('LBR', '['),
            ('RBR', ']'),
            ('string', 'symbol', 'string'),
            ('string', 'empty'),
            ('symbol', 'LETTER', 'number'),
            ('number', 'NUMBER', 'number'),
            ('number', 'empty'),
            )

        lexer = lex.lex(module=Lexer(M))
        lexer.input('A21[]')

        self.assertEqual(list(get_tokens(lexer)), [
            ('LETTER', 'A'),
            ('NUMBER', '2'),
            ('NUMBER', '1'),
            ('LBR', '['),
            ('RBR', ']')
            ]
                             )
        lexer.input('A21X[]')

        with self.assertWarns(UserWarning):
            list(get_tokens(lexer))


if __name__ == '__main__':
    unittest.main(verbosity=2)
