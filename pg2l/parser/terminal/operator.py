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
        self.tokens.append(grammar.name)
        self.operators.append(operator)
        # setattr(self, 't_%s' % grammar_operator, r'%s' % operator)
        setattr(Operator, 't_%s' % grammar.name, staticmethod(lambda x: x))
        getattr(Operator, 't_%s' % grammar.name).__doc__ = r'\%s' % operator
        getattr(Operator, 't_%s' % grammar.name).__name__ = grammar.name
        getattr(Operator, 't_%s' % grammar.name).__qualname__ = grammar.name

@register_with_terminal(G.REWRITE.name)
class RewriteLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_REWRITE):
        Operator.__init__(self, operator, G.REWRITE)

@register_with_terminal(G.GLCONTEXT.name)
class GLContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_GLCONTEXT):
        Operator.__init__(self, operator, G.GLCONTEXT)

@register_with_terminal(G.GRCONTEXT.name)
class GRContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_GRCONTEXT):
        Operator.__init__(self, operator, G.GRCONTEXT)

@register_with_terminal(G.SLCONTEXT.name)
class SLContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_SLCONTEXT):
        Operator.__init__(self, operator, G.SLCONTEXT)

@register_with_terminal(G.SRCONTEXT.name)
class SRContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_SRCONTEXT):
        Operator.__init__(self, operator, G.SRCONTEXT)

