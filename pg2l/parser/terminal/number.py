# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import BaseLexer
from pg2l import grammar

@grammar.register('NUMBER')
class NumberLexer(BaseLexer, grammar.Terminal):
    def __init__(self, *numbers):
        self.tokens += [grammar.Grammar.NUMBER]
        self.variables += [str(x) for x in numbers]
        numbers = [str(x) for x in numbers]
        NumberLexer.t_NUMBER.__doc__ = r'|'.join(['%s' % i for i in numbers])

    def t_NUMBER(self, t):
        t.value = int(t.value)
        return t
