# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from collections import defaultdict

import networkx as nx

from .base import AbstractTerminalSymbol, MetaDeclaration as G

from pg2l.grammar import AbstractGrammar


class MetaGrammar(AbstractGrammar):
    
    def __init__(self, *declarations):
        axiom, *productions = declarations
        super().__init__(axiom, productions)
        self.declarations = declarations
        
        self._axiom = axiom.symbol
        self._terminals = {}
        self._nonterminals = defaultdict(lambda:list())
        self._productions = []

        
        for lhs, *rhs in productions:
            if lhs in G.terminals:
                self._terminals[lhs.symbol] = [x for x in rhs[0]]
            elif lhs in G.nonterminals:
                self._nonterminals[lhs.symbol] = [x.symbol for x in rhs]
            else:
                raise TypeError(lhs)

        self.derivation_graph = nx.DiGraph()
        for lhs, rhs in self._nonterminals.items():
            for sym in rhs:
                self.derivation_graph.add_edge(lhs, sym, rhs=rhs)


    @property
    def terminals(self):
        return set(self._terminals.keys())

    @property
    def nonterminals(self):
        return set(self._nonterminals.keys())
    
    @property
    def axiom(self):
        return set([self._axiom])
    
    @property
    def productions(self):
        return ['%s -> %s' % (lhs, ' '.join(rhs)) for lhs,rhs in self._nonterminals.items()]
    
    def generate(self, max_recursion=-1):
        raise NotImplementedError()

    def __repr__(self):
        return ''


