# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
import ply.lex as lex

from pg2l.parser.mixin import mixin, AbstractMixin

class LexerMixin(AbstractMixin):
    pass

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

# def lexer_factory(*params):
#     params = [(BaseLexer, (), {})] + list([x for x in params if x])
#     lexer_class = [x[0] for x in params]

#     class _Lexer(*lexer_class[1:]):
#         def __init__(self):
#             for aclass, args, kwargs in params:
#                 print('params', aclass, args, kwargs)
#                 aclass.__init__(self, *args, **kwargs)

#     return _Lexer().build()
