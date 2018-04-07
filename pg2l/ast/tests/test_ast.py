# -*- coding : utf-8 -*-
import unittest

from pg2l.ast import ast

class TestAstAst(unittest.TestCase):
    def test_empty(self):
        e = ast.Empty()
        self.assertEqual(str(e), '')
        self.assertEqual(e.data, dict(symbol=''))
        self.assertEqual(repr(e), '(ε)')

    def test_SYM(self):
        l = ast.Symbol(symbol='A')
        r = ast.Round()
        j = ast.Jump(jump=1)
        s = ast.SYM()
        r.push(j)
        s.push(l)
        s.push(r)
        self.assertEqual(repr(s), '(SYM A1)')
        self.assertEqual(str(s), 'A1')
        self.assertEqual([repr(x) for x in s], ['(SYM A1)', '(Symbol A)', '(Round 1)', '(Jump 1)'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
