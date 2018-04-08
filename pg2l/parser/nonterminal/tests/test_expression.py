# -*- coding : utf-8 -*-
import unittest

from pg2l.grammar import Grammar as G, terminals
from pg2l.parser.terminal.base import lexer_factory
from pg2l.parser.nonterminal.base import mixin_builder, nonterminals, BaseParser

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
        lexer = lexer_factory((terminals[G.LETTER], ('ABCD',), {}),
                              (terminals[G.NUMBER], (-1,0,1), {}),
                              (terminals[G.LBR], ('[',), {}),
                              (terminals[G.RBR], (']',), {})
                                  )
        lexer.lexer.input('A1[BB]')

        parser = mixin_builder(
            (BaseParser, (), {}),
            (nonterminals[G.expression], (), {}),
            (nonterminals[G.node], (), {}),)

        parser.build(lexer)
        self.assertEqual(repr(parser.parse('ABCD')), '(AXIOM ABCD)')

if __name__ == '__main__':
    unittest.main(verbosity=2)
