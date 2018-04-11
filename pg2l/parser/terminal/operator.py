# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import LexerMixin, register_with_terminal

from pg2l.ast import Grammar as G


DEFAULT_OP_REWRITE = ':'   # rewrite operator
DEFAULT_OP_GLCONTEXT = '<' # graph left-context operator
DEFAULT_OP_GRCONTEXT = '>' # graph right-context operator
DEFAULT_OP_SLCONTEXT = '{' # string left-context operator
DEFAULT_OP_SRCONTEXT = '}' # string right-context operator


class Operator(LexerMixin):
    def __init__(self, operator, grammar_operator):
        self.tokens.append(grammar_operator)
        self.operators.append(operator)
        setattr(self, 't_%s' % grammar_operator, r'%s' % operator)

@register_with_terminal(G.OP_REWRITE.name)
class RewriteLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_REWRITE):
        Operator.__init__(self, operator, G.OP_REWRITE.name)

@register_with_terminal(G.OP_GLCONTEXT.name)
class GLContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_GLCONTEXT):
        Operator.__init__(self, operator, G.OP_GLCONTEXT.name)

@register_with_terminal(G.OP_GRCONTEXT.name)
class GRContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_GRCONTEXT):
        Operator.__init__(self, operator, G.OP_GRCONTEXT.name)

@register_with_terminal(G.OP_SLCONTEXT.name)
class SLContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_SLCONTEXT):
        Operator.__init__(self, operator, G.OP_SLCONTEXT.name)

@register_with_terminal(G.OP_SRCONTEXT.name)
class SRContextLexer(Operator):
    def __init__(self, operator=DEFAULT_OP_SRCONTEXT):
        Operator.__init__(self, operator, G.OP_SRCONTEXT.name)

