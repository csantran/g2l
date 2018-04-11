# -*- coding : utf-8 -*-
import unittest

from pg2l.parser.mixin import mixin
from pg2l.parser.terminal.base import BaseLexer, terminals
from pg2l.ast import Grammar as G

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
            (terminals[G.LETTER.name], ('ABCD',), {}),)
        lexer.build()
        lexer.lexer.input('A')

        self.assertEqual(get_tokens(lexer), [('LETTER', 'A')])

        lexer.lexer.input('Z')
        self.assertEqual(get_tokens(lexer), [])

    def test_number(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.NUMBER.name], (-1,0,1), {}),)

        lexer.build()
        lexer.lexer.input('10-1')

        self.assertEqual(get_tokens(lexer), [('NUMBER', 1), ('NUMBER', 0), ('NUMBER', -1)])

        lexer.lexer.input('2')
        self.assertEqual(get_tokens(lexer), [])

    def test_constants(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.name], ('[',), {}),)

        lexer.build()
        lexer.lexer.input('[')

        self.assertEqual(get_tokens(lexer), [('LBR', '[')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.RBR.name], (']',), {}),)
        lexer.build()
        lexer.lexer.input(']')

        self.assertEqual(get_tokens(lexer), [('RBR', ']')])
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.name], ('['), {}),
                          (terminals[G.RBR.name], (']'), {}))
        lexer.build()
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.name], (), {}),
                          (terminals[G.RBR.name], (), {}))

        lexer.build()
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LBR.name], ('('), {}),
                          (terminals[G.RBR.name], (')'), {}))

        lexer.build()
        lexer.lexer.input('()')

        self.assertEqual(get_tokens(lexer), [('LBR', '('), ('RBR', ')')])

    def test_operator(self):
        lexer = mixin('LexerMixin',
            (BaseLexer, (), {}),
            (terminals[G.OP_REWRITE.name], (), {}),
            (terminals[G.OP_GLCONTEXT.name], (), {}),
            (terminals[G.OP_GRCONTEXT.name], (), {}),
            (terminals[G.OP_SLCONTEXT.name], (), {}),
            (terminals[G.OP_SRCONTEXT.name], (), {})
            )

        lexer.build()
        lexer.lexer.input(':<>{}')
        self.assertEqual(get_tokens(lexer), [
            ('OP_REWRITE', ':'),
            ('OP_GLCONTEXT', '<'),
            ('OP_GRCONTEXT', '>'),
            ('OP_SLCONTEXT', '{'),
            ('OP_SRCONTEXT', '}')
            ])

        lexer = mixin('LexerMixin',
            (BaseLexer, (), {}),
            (terminals[G.OP_REWRITE.name], ('⇒'), {}),
            (terminals[G.OP_GLCONTEXT.name], ('↢'), {}),
            (terminals[G.OP_GRCONTEXT.name], ('↣'), {}),
            (terminals[G.OP_SLCONTEXT.name], ('↤'), {}),
            (terminals[G.OP_SRCONTEXT.name], ('↦'), {})
            )

        lexer.build()
        lexer.lexer.input('⇒↢↣↤↦')
        self.assertEqual(get_tokens(lexer), [
            ('OP_REWRITE', '⇒'),
            ('OP_GLCONTEXT', '↢'),
            ('OP_GRCONTEXT', '↣'),
            ('OP_SLCONTEXT', '↤'),
            ('OP_SRCONTEXT', '↦')])

if __name__ == '__main__':
    unittest.main(verbosity=2)
