# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from collections import defaultdict

from .base import AbstractTerminalSymbol

from pg2l.grammar import AbstractGrammar

class MetaGrammar(AbstractGrammar):
    
    def __init__(self, axiom, *productions):
        super().__init__()
        self._terminals = {}
        self._nonterminals = defaultdict(lambda:list())
        self._axiom = None

        for lhs, *rhs in productions:
            print(lhs, rhs)
            if isinstance(lhs, AbstractTerminalSymbol):
                self._terminals[lhs.name] = rhs

        print(self._terminals)

    @property
    def nonterminals(self):
        pass
    
    @property
    def axiom(self):
        pass
    
    @property
    def productions(self):
        pass
    
    def generate(self, max_recursion=-1):
        raise NotImplementedError()

    def __repr__(self):
        return ''


