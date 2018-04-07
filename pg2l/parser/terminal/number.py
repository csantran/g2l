# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from pg2l import grammar

@grammar.register('NUMBER')
class NumberLexer(grammar.Terminal):
    def __init__(self, *numbers):
        self.tokens += [grammar.Grammar.NUMBER]
        self.variables += [str(x) for x in numbers]
        numbers = [str(x) for x in numbers]

        pattern =  r'|'.join(['%s' % i for i in numbers])

        NumberLexer.t_NUMBER.__doc__ = pattern % numbers # TODO, % numbers ???

    def t_NUMBER(self, t):
        t.value = int(t.value)
        return t
