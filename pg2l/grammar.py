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

terminals = {}
nonterminals = {}

def register(element, *others):

    def __register_element_with(this_cls=None):
        if this_cls:
            bases = inspect.getmro(this_cls)

            if Terminal in bases:
                terminals[element] = this_cls
            elif NonTerminal in bases:
                nonterminals[element] = this_cls
            else:
                raise TypeError(this_cls)

        return this_cls

    if hasattr(Grammar, element):
        raise AttributeError(element)

    setattr(Grammar, element, element)

    for o in others:
        setattr(Grammar, o, o)

    return __register_element_with

