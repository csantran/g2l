# -*- coding : utf-8 -*-
import unittest

from pg2l.parser.nonterminal.base import nonterminals, BaseParser
from pg2l.parser.terminal.base import terminals, BaseLexer
from pg2l.parser.mixin import mixin
from pg2l.ast import Grammar as G


def get_tokens(lexer):
    toks = []
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        toks.append(tok)

    return [(x.type, x.value) for x in toks]

class TestExpression(unittest.TestCase):
    def test_expression(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {}),
                          (terminals[G.LETTER.name], ('ABCD',), {}),
                              (terminals[G.NUMBER.name], (-1,0,1), {}),
                              (terminals[G.LBR.name], ('[',), {}),
                              (terminals[G.RBR.name], (']',), {})
                                  )
        lexer.build()
        lexer.lexer.input('A1[BB]')

        parser = mixin('MixinParser',
            (BaseParser, (), {}),
            (nonterminals[G.expression.name], (), {}),
            (nonterminals[G.node.name], (), {}),)

        parser.build(lexer)

        self.assertEqual(repr(parser),"""
#from p_axiom_level
axiom : level

#from p_basenode_node
basenode : node

#from p_expression_axiom
expression : axiom

#from p_letter
label : LETTER

#from p_level_basenode
level : basenode
\t| level basenode

#from p_node
node : label""")
        
        self.assertEqual(repr(parser.parse('ABCD')), '(axiom ABCD)')
        self.assertEqual(str(type(parser)), "<class 'pg2l.parser.mixin.MixinParser'>")
        self.assertIsInstance(parser, BaseParser)
        self.assertEqual(repr(parser.parse('ABZCD')), '(axiom ABCD)')

    def test_p_error(self):
        lexer = mixin('LexerMixin',
                          (BaseLexer, (), {'strict':True}),
                          (terminals[G.LETTER.name], ('ABCD',), {}),
                              (terminals[G.NUMBER.name], (-1,0,1), {}),
                              (terminals[G.LBR.name], ('[',), {}),
                              (terminals[G.RBR.name], (']',), {})
                                  )
        lexer.build()
        lexer.lexer.input('A1[BB]')

        parser = mixin('MixinParser',
            (BaseParser, (), {'strict':True}),
            (nonterminals[G.expression.name], (), {}),
            (nonterminals[G.node.name], (), {}),)

        parser.build(lexer)

        with self.assertRaises(ValueError):
            parser.parse('Z')

        with self.assertRaises(EOFError):
            parser.parse('')

        with self.assertRaises(SyntaxError):
            parser.parse('1A')


if __name__ == '__main__':
    unittest.main(verbosity=2)
