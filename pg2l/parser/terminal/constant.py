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


DEFAULT_LBR = '['
DEFAULT_RBR = ']'


class Constant(LexerMixin):
    def __init__(self, constant, grammar):
        self.tokens.append(grammar.name)
        self.constants.append(constant)
        
        setattr(Constant, 't_%s' % grammar.name, staticmethod(lambda x: x))
        getattr(Constant, 't_%s' % grammar.name).__doc__ = r'\%s' % constant
        getattr(Constant, 't_%s' % grammar.name).__name__ = grammar.name
        getattr(Constant, 't_%s' % grammar.name).__qualname__ = grammar.name

@register_with_terminal(G.LBR.name)
class LBRLexer(Constant):
    def __init__(self, constant=DEFAULT_LBR, grammar=G.LBR):
        Constant.__init__(self, constant, G.LBR)

@register_with_terminal(G.RBR.name)
class RBRLexer(Constant):
    def __init__(self, constant=DEFAULT_RBR):
        Constant.__init__(self, constant, G.RBR)
