# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import LexerMixin, register_with_terminal
from pg2l import grammar
from pg2l.grammar import Grammar as G


@register_with_terminal(G.NUMBER)
class NumberLexer(LexerMixin, grammar.Terminal):
    def __init__(self, *numbers):
        self.tokens += [G.NUMBER]
        self.variables += [str(x) for x in numbers]
        numbers = [str(x) for x in numbers]
        NumberLexer.t_NUMBER.__doc__ = r'|'.join(['%s' % i for i in numbers])

    @staticmethod
    def t_NUMBER(t):
        t.value = int(t.value)
        return t
