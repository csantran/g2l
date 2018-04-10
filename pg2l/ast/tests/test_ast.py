# -*- coding : utf-8 -*-
import unittest

from pg2l.ast import ast

class TestAstAst(unittest.TestCase):
    def test_empty(self):
        e = ast.Empty()
        self.assertEqual(str(e), '')
        self.assertEqual(e.value, '')

    def test_SYM(self):
        l = ast.Letter('A')
        r = ast.Round()
        j = ast.Jump(1)
        s = ast.JNode()
        r.push(j)
        s.push(l)
        s.push(r)
        self.assertEqual(repr(s), '(jnode A1)')
        self.assertEqual(str(s), 'A1')
        self.assertEqual([repr(x) for x in s], ['(jnode A1)', '(letter A)', '(round 1)', '(jump 1)'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
