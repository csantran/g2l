# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
import inspect

class Terminal(object):
    pass

class NonTerminal(object):
    pass

class Grammar(object):
    pass

def register(element, *others):
    if hasattr(Grammar, element):
        raise AttributeError(element)

    setattr(Grammar, element, element)

    for o in others:
        setattr(Grammar, o, o)

register('LETTER')
register('OP_REWRITE', 'OP_GLCONTEXT', 'OP_GRCONTEXT', 'OP_SLCONTEXT', 'OP_SRCONTEXT')
register('LBR', 'RBR')
register('NUMBER')

register('basenode', 'node', 'letter')
register('expression', 'axiom', 'level')




