# -*- coding : utf-8 -*-
import unittest

from pg2l.grammar.grammar import MetaGrammar

class TestMetaGrammar(unittest.TestCase):

    def test_meta_grammar(self):

        M = MetaGrammar.from_declaration(
            ('S', 'F'),
            ('S', '(', 'S', '+', 'F', ')'),
            ('F', '1'),
            )

        self.assertEqual(M.axiom, 'S')
        self.assertEqual(M.terminals, {'(', ')', '1', '+'})
        self.assertEqual(M.nonterminals, {'S', 'F'})

        self.assertEqual(sorted(list(M.productions)), sorted([
            ('S', ('(', 'S', '+', 'F', ')')),
            ('S', ('F',)),
            ('F', ('1',)),
            ]))

        self.assertEqual(M.alphabet, {'(', '+', 'S', 'F', '1', ')'})


if __name__ == '__main__':
    unittest.main(verbosity=2)
