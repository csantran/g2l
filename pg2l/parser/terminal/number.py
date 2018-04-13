# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import LexerMixin, register_with_terminal
from pg2l.ast import MetaDeclaration as G

def num(t):
    t.value = int(t.value)
    return t

@register_with_terminal(G.NUMBER.symbol)
class NumberLexer(LexerMixin):
    def __init__(self, *numbers):
        self.tokens += [G.NUMBER.symbol]
        self.variables += [str(x) for x in numbers]
        numbers = [str(x) for x in numbers]

        setattr(NumberLexer, 't_%s' % G.NUMBER.symbol, staticmethod(num))
        getattr(NumberLexer, 't_%s' % G.NUMBER.symbol).__doc__ = r'|'.join(['%s' % i for i in numbers])
        getattr(NumberLexer, 't_%s' % G.NUMBER.symbol).__symbol__ = G.NUMBER.symbol
        getattr(NumberLexer, 't_%s' % G.NUMBER.symbol).__qualsymbol__ = G.NUMBER.symbol


