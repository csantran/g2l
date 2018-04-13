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


DEFAULT_OP_REWRITE = ':'   # rewrite operator
DEFAULT_OP_GLCONTEXT = '<' # graph left-context operator
DEFAULT_OP_GRCONTEXT = '>' # graph right-context operator
DEFAULT_OP_SLCONTEXT = '{' # string left-context operator
DEFAULT_OP_SRCONTEXT = '}' # string right-context operator


class Operator(LexerMixin):
    def __init__(self, operator, grammar):
        self.tokens.append(grammar.symbol)
        self.operators.append(operator)
        # setattr(self, 't_%s' % grammar_operator, r'%s' % operator)
        setattr(Operator, 't_%s' % grammar.symbol, staticmethod(lambda x: x))
        getattr(Operator, 't_%s' % grammar.symbol).__doc__ = r'\%s' % operator
        getattr(Operator, 't_%s' % grammar.symbol).__symbol__ = grammar.symbol
        getattr(Operator, 't_%s' % grammar.symbol).__qualsymbol__ = grammar.symbol

@register_with_terminal(G.REWRITE.symbol)
class RewriteLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_REWRITE):
        Operator.__init__(self, operator, G.REWRITE)

@register_with_terminal(G.GLCONTEXT.symbol)
class GLContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_GLCONTEXT):
        Operator.__init__(self, operator, G.GLCONTEXT)

@register_with_terminal(G.GRCONTEXT.symbol)
class GRContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_GRCONTEXT):
        Operator.__init__(self, operator, G.GRCONTEXT)

@register_with_terminal(G.SLCONTEXT.symbol)
class SLContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_SLCONTEXT):
        Operator.__init__(self, operator, G.SLCONTEXT)

@register_with_terminal(G.SRCONTEXT.symbol)
class SRContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_SRCONTEXT):
        Operator.__init__(self, operator, G.SRCONTEXT)

