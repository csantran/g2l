# -*- coding : utf-8 -*-
import unittest

from pg2l.grammar import Grammar, terminals
from pg2l.parser.mixin import mixin
from pg2l.parser.terminal.base import BaseLexer

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
            (terminals[Grammar.LETTER], ('ABCD',), {}),)
        lexer.build()
        lexer.lexer.input('A')

        self.assertEqual(get_tokens(lexer), [('LETTER', 'A')])

        lexer.lexer.input('Z')
        self.assertEqual(get_tokens(lexer), [])

    def test_number(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[Grammar.NUMBER], (-1,0,1), {}),)

        lexer.build()
        lexer.lexer.input('10-1')

        self.assertEqual(get_tokens(lexer), [('NUMBER', 1), ('NUMBER', 0), ('NUMBER', -1)])

        lexer.lexer.input('2')
        self.assertEqual(get_tokens(lexer), [])

    def test_constants(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[Grammar.LBR], ('[',), {}),)

        lexer.build()
        lexer.lexer.input('[')

        self.assertEqual(get_tokens(lexer), [('LBR', '[')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[Grammar.RBR], (']',), {}),)
        lexer.build()
        lexer.lexer.input(']')

        self.assertEqual(get_tokens(lexer), [('RBR', ']')])
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[Grammar.LBR], ('['), {}),
                          (terminals[Grammar.RBR], (']'), {}))
        lexer.build()
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[Grammar.LBR], (), {}),
                          (terminals[Grammar.RBR], (), {}))
        
        lexer.build()
        lexer.lexer.input('[]')

        self.assertEqual(get_tokens(lexer), [('LBR', '['), ('RBR', ']')])

        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[Grammar.LBR], ('('), {}),
                          (terminals[Grammar.RBR], (')'), {}))
        
        lexer.build()
        lexer.lexer.input('()')

        self.assertEqual(get_tokens(lexer), [('LBR', '('), ('RBR', ')')])

    def test_operator(self):
        lexer = mixin('LexerMixin',
            (BaseLexer, (), {}),
            (terminals[Grammar.OP_REWRITE], (), {}),
            (terminals[Grammar.OP_GLCONTEXT], (), {}),
            (terminals[Grammar.OP_GRCONTEXT], (), {}),
            (terminals[Grammar.OP_SLCONTEXT], (), {}),
            (terminals[Grammar.OP_SRCONTEXT], (), {})
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
            (terminals[Grammar.OP_REWRITE], ('⇒'), {}),
            (terminals[Grammar.OP_GLCONTEXT], ('↢'), {}),
            (terminals[Grammar.OP_GRCONTEXT], ('↣'), {}),
            (terminals[Grammar.OP_SLCONTEXT], ('↤'), {}),
            (terminals[Grammar.OP_SRCONTEXT], ('↦'), {})
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
