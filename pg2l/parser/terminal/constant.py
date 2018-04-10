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


DEFAULT_LBR = '['
DEFAULT_RBR = ']'


class Constant(LexerMixin, grammar.Terminal):
    def __init__(self, constant, grammar_constant):
        self.tokens += [grammar_constant]
        self.constants += [constant]
        setattr(self, 't_%s' % grammar_constant, r'\%s' % constant)

@register_with_terminal(G.LBR)
class LBRLexer(Constant):
    def __init__(self, constant=DEFAULT_LBR):
        Constant.__init__(self, constant, G.LBR)

@register_with_terminal(G.RBR)
class RBRLexer(Constant):
    def __init__(self, constant=DEFAULT_RBR):
        Constant.__init__(self, constant, G.RBR)
