# -*- coding : utf-8 -*-
import unittest

from pg2l.grammar import Grammar as G
from pg2l.parser.nonterminal.base import nonterminals, BaseParser
from pg2l.parser.terminal.base import terminals, BaseLexer
from pg2l.parser.mixin import mixin


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
                          (terminals[G.LETTER], ('ABCD',), {}),
                              (terminals[G.NUMBER], (-1,0,1), {}),
                              (terminals[G.LBR], ('[',), {}),
                              (terminals[G.RBR], (']',), {})
                                  )
        lexer.build()
        lexer.lexer.input('A1[BB]')

        parser = mixin('MixinParser',
            (BaseParser, (), {}),
            (nonterminals[G.expression], (), {}),
            (nonterminals[G.node], (), {}),)

        print(repr(parser))
        parser.build(lexer)
        self.assertEqual(repr(parser.parse('ABCD')), '(axiom ABCD)')
        self.assertEqual(str(type(parser)), "<class 'pg2l.parser.mixin.MixinParser'>")
        self.assertIsInstance(parser, BaseParser)

if __name__ == '__main__':
    unittest.main(verbosity=2)
