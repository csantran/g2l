# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
import ply.lex as lex

from pg2l.parser.base import decorator_register_factory
from pg2l.parser.mixin import AbstractMixin

class LexerMixin(AbstractMixin):
    """Lexer Mixin base class"""

class BaseLexer(LexerMixin):
    def __init__(self):
        self.lexer = None
        self.tokens = []
        self.variables = []
        self.constants = []
        self.operators = []

    @property
    def alphabet(self): return frozenset(set(self.variables) | set(self.constants))

    @staticmethod
    def t_error(t):
        print("warning:g2l.lexer: error, illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def __iter__(self):
        return iter(self.lexer)

    def token(self):
        return self.lexer.token()

    def input(self, data):
        self.lexer.input(data)

    def build(self):
        self.lexer = lex.lex(module=self)
        return self

terminals = {}

register_with_terminal = decorator_register_factory(terminals)
