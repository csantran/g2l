# -*- coding : utf-8 -*-
import unittest

from pg2l.parser.mixin import mixin
from pg2l.parser.terminal.base import BaseLexer, terminals
from pg2l.ast import MetaDeclaration as G

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
        lexer = mixin('LexerMixin',
            (BaseLexer, (), {}),
            (terminals[G.LETTER.symbol], ('ABCD',), {}),)
        lexer.build()
        lexer.lexer.input('A')

        self.assertEqual(get_tokens(lexer), [('LETTER', 'A')])

        lexer.lexer.input('Z')
        self.assertEqual(get_tokens(lexer), [])

    def test_number(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.NUMBER.symbol], (-1,0,1), {}),)

        lexer.build()
        lexer.lexer.input('10-1')

        self.assertEqual(get_tokens(lexer), [('NUMBER', 1), ('NUMBER', 0), ('NUMBER', -1)])

        lexer.lexer.input('2')
        self.assertEqual(get_tokens(lexer), [])

    def test_constants(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.symbol], ('[',), {}),)

        lexer.build()
        lexer.lexer.input('[')

        self.assertEqual(get_tokens(lexer), [('LBR', '[')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.RBR.symbol], (']',), {}),)
        lexer.build()
        lexer.lexer.input(']')

        self.assertEqual(get_tokens(lexer), [('RBR', ']')])
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.symbol], ('['), {}),
                          (terminals[G.RBR.symbol], (']'), {}))
        lexer.build()
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.symbol], (), {}),
                          (terminals[G.RBR.symbol], (), {}))

        lexer.build()
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.symbol], ('('), {}),
                          (terminals[G.RBR.symbol], (')'), {}))

        lexer.build()
        lexer.lexer.input('()')

        self.assertEqual(get_tokens(lexer), [('LBR', '('), ('RBR', ')')])

    def test_operator(self):
        lexer = mixin('LexerMixin',
            (BaseLexer, (), {}),
            (terminals[G.REWRITE.symbol], (), {}),
            (terminals[G.GLCONTEXT.symbol], (), {}),
            (terminals[G.GRCONTEXT.symbol], (), {}),
            (terminals[G.SLCONTEXT.symbol], (), {}),
            (terminals[G.SRCONTEXT.symbol], (), {})
            )

        lexer.build()
        lexer.lexer.input(':<>{}')
        self.assertEqual(get_tokens(lexer), [
            ('REWRITE', ':'),
            ('GLCONTEXT', '<'),
            ('GRCONTEXT', '>'),
            ('SLCONTEXT', '{'),
            ('SRCONTEXT', '}')
            ])

        lexer = mixin('LexerMixin',
            (BaseLexer, (), {}),
            (terminals[G.REWRITE.symbol], ('⇒'), {}),
            (terminals[G.GLCONTEXT.symbol], ('↢'), {}),
            (terminals[G.GRCONTEXT.symbol], ('↣'), {}),
            (terminals[G.SLCONTEXT.symbol], ('↤'), {}),
            (terminals[G.SRCONTEXT.symbol], ('↦'), {})
            )

        lexer.build()
        lexer.lexer.input('⇒↢↣↤↦')
        self.assertEqual(get_tokens(lexer), [
            ('REWRITE', '⇒'),
            ('GLCONTEXT', '↢'),
            ('GRCONTEXT', '↣'),
            ('SLCONTEXT', '↤'),
            ('SRCONTEXT', '↦')])

if __name__ == '__main__':
    unittest.main(verbosity=2)
