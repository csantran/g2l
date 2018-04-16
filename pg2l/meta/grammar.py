# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from collections import defaultdict
from functools import reduce


import networkx as nx
import networkx.algorithms as al

# from pg2l.grammar import AbstractGrammar
def production_to_string(production):
    lhs, rhs = production[0], production[1:]
    return '%s := %s' % (lhs, ' '.join(rhs))

def check_args(condition, exception):
    def _check_args(decorated):
        def __check_decorated(*args):
            if not condition(*args):
                raise exception('bad statement: %s' % str(args))

            return decorated(*args)

        return __check_decorated
    return _check_args

class MetaGrammar(object):
    
    def __init__(self, *declarations, strict=False):
        super().__init__()
        self.derivation_graph = nx.DiGraph()

        for dec in declarations:
            
            lhs, rhs = dec[0], dec[1:]

            if lhs == 'S':
                self.__add_nonterminal(*dec)

            else:
                if lhs.isupper():
                    self.__add_terminal(*dec)

                elif lhs.islower():
                    self.__add_nonterminal(*dec)
                else:
                    raise SyntaxError('bad statement %s' % dec)

        for n in self.derivation_graph.nodes:
            if not nx.has_path(self.derivation_graph, 'S', n):
                raise Exception('unreachable symbol %s' % n)
            
        without_cycle = nx.DiGraph()
        for n in self.derivation_graph.nodes():
            without_cycle.add_path(nx.shortest_path(self.derivation_graph,'S',n))

        for cycle in al.cycles.simple_cycles(self.derivation_graph):
            if len(cycle) > 1:
                w = nx.DiGraph()
                longest = (0, None)
                
                for n in cycle:
                    path = nx.shortest_path(self.derivation_graph,'S', n)
                    w.add_path(path)
                    if len(path) > longest[0]:
                        longest = (len(path), n)

                diff = al.operators.difference(self.derivation_graph.subgraph(w.nodes), w)
                raise Exception('ambiguous context-free grammar, cycle found:  %s -> %s' % (
                    longest[1],
                    str([x for x in self.derivation_graph.successors(longest[1]) if x in w.nodes])
                    ))

    @check_args(lambda *args: len(args) != 3, SyntaxError)
    def __add_terminal(self, name, values, t_type):

        if isinstance(values, str):
            values = list(values)

        v_set = set(values)

        if len(values) != len(v_set):
            raise Exception('terminal values must be a set of unique object, duplicates found in %s := %s' % (name, str(values)))

        self.derivation_graph.add_node(name, type=t_type)

        values_str = '|'.join(str(x) for x in values)
        self.derivation_graph.add_edge(name, values_str, production=[(name, values_str)])
        self.derivation_graph.nodes[values_str]['values'] = set(values)
        self.derivation_graph.nodes[values_str]['type'] = t_type

    def __add_nonterminal(self, *declaration):
        lhs, rhs = declaration[0], declaration[1:]

        for symbol in rhs:
            if not self.derivation_graph.has_edge(lhs, symbol):
                self.derivation_graph.add_edge(lhs, symbol, production=[declaration])
            else:
                if declaration not in self.derivation_graph[lhs][symbol]['production']:
                    self.derivation_graph[lhs][symbol]['production'].append(declaration)

            
    @property
    def terminals(self):
        # return set(self._terminals.keys())
        pass

    @property
    def nonterminals(self):
        # return set(self._nonterminals.keys())
        pass
    
    @property
    def axiom(self):
        # return set([self._axiom])
        pass
    
    @property
    def productions(self):
        # return ['%s -> %s' % (lhs, ' '.join(rhs)) for lhs,rhs in self._nonterminals.items()]
        pass
    
    def generate(self, max_recursion=-1):
        raise NotImplementedError()

    def __repr__(self):
        grammar_prods = []
        
        without_cycle = nx.DiGraph()
        for n in self.derivation_graph.nodes():
            without_cycle.add_path(nx.shortest_path(self.derivation_graph,'S',n))


        for n in nx.topological_sort(
            al.operators.intersection(
                    self.derivation_graph,
                    without_cycle)):

            if self.derivation_graph.out_degree(n):
                productions = sorted([p for successor in self.derivation_graph.successors(n)
                                                for p in self.derivation_graph[n][successor]['production']],
                                                key=len)

                prod = []
                for x in productions:
                    if x and x not in prod:
                        prod.append(x)

                grammar_prods.append('%s := %s' % (prod[0][0], ' '.join(prod[0][1:])))

                if len(prod) > 1:
                    for p in prod[1:]:
                        grammar_prods.append(' | %s' % ' '.join(p[1:]))

        return '\n'.join(grammar_prods)

