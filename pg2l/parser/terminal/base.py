# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
import ply.lex as lex
from inspect import ismethod

from pg2l.parser.base import decorator_register_factory
from pg2l.parser.mixin import AbstractMixin

class LexerMixin(AbstractMixin):
    """Lexer Mixin base class"""

class BaseLexer(LexerMixin):
    def __init__(self, strict=False):
        self.__strict = strict
        self.lexer = None
        self.tokens = []
        self.variables = []
        self.constants = []
        self.operators = []

    @property
    def alphabet(self): return frozenset(set(self.variables) | set(self.constants))

    def t_error(self, t):
        if self.__strict:
            raise ValueError("pg2l.lexer: error, illegal character '%s'" % t.value[0])
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

    def __repr__(self):
        repr_string = []

        for name in dir(self):
            if name.startswith('t_') and name not in ('t_error', '__init__'):
                method = getattr(self, name)
                repr_string.append('\n#from %s' % method)

                for line in [l.strip() for l in method.__doc__.split('\n')]:
                    if line:

                        repr_string.append((line.startswith('|') \
                                                and '\t%s' % line \
                                                or '%s : %s' % (method.__name__, line)))

        return '\n'.join(repr_string)

terminals = {}

register_with_terminal = decorator_register_factory(terminals)
