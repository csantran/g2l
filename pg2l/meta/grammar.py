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
import types

import networkx as nx
import networkx.algorithms as al


from .declaration import VAR, CONST, S, META, SELF

# from pg2l.grammar import AbstractGrammar

class Grammar(object):

    def __init__(self, graph=None):
        self.graph = graph or nx.DiGraph()

    @property
    def axiom(self):
        axiom = [n for n in self.graph.nodes() if not
                     [p for p in self.graph.predecessors(n) if p != n]]
        
        if len(axiom) > 1:
            raise Exception(axiom)

        return axiom[0]

    @property
    def terminals(self):
        return set([n for n in self.graph.nodes() if
                            self.graph.out_degree(n) == 0 and n != 'ε'])

    @property
    def nonterminals(self):
        return self.alphabet - self.terminals
        
    @property
    def alphabet(self):
        return set(self.graph.nodes())

    @property
    def productions(self):
        for u,v,data in self.graph.edges(data=True):
            for prod in data['production']:
                yield (u, prod)

    def __add__(self, grammar):
        return Grammar(nx.compose(self.graph, grammar.graph))

#################
def check_declaration(declaration):
    lhs, rhs = declaration[0], declaration[1:]
    
    if not (len(rhs) == 1 and isinstance(rhs[0], (list, tuple, types.GeneratorType, range))):
        if set([META, SELF]) & set(rhs):
            raise SyntaxError()

def add_production(graph, declaration):
    check_declaration(declaration)
    lhs, rhs = declaration[0], declaration[1:]

    if lhs not in graph.nodes:
        graph.add_node(lhs)

    if len(rhs) == 1 and isinstance(rhs[0], (list, tuple, types.GeneratorType, range)):
        for symbol in rhs[0]:
            if graph.has_edge(lhs, symbol):
                raise Exception()
            else:
                graph.add_edge(lhs, symbol, production=[[symbol]])
    else:
        
        for symbol in rhs:
            if graph.has_edge(lhs, symbol):
                graph[lhs][symbol]['production'].append(rhs)
            else:
                graph.add_edge(lhs, symbol, production=[rhs])

def build(*declarations):
    G = Grammar()
    
    for declaration in declarations:
        add_production(G.graph, declaration)

    return G


###############################################"
# def get_first(graph):
#     return get_subgraph_by_edge_property(graph, eproperty='1')

# def get_subgraph_by_edge_property(graph, eproperty):
#     edges = ((u,v,data) for u,v,data in graph.edges(data=True) if eproperty in data)
#     sub = nx.DiGraph(edges)

#     for u,v,data in list(sub.edges(data=True)):
#         if eproperty not in data:
#             sub.remove_edge(u,v)

#     return sub
# def production_to_string(production):
#     lhs, rhs = production[0], production[1:]
#     return '%s := %s' % (lhs, ' '.join(rhs))

# def check_args(condition, exception):
#     def _check_args(decorated):
#         def __check_decorated(*args):
#             if not condition(*args):
#                 raise exception('bad statement: %s' % str(args))

#             return decorated(*args)

#         return __check_decorated
#     return _check_args


                # if i == 0:
                #     if str(i+1) in self.graph[lhs][symbol]:
                #         raise Exception("it's a grammar LL (1), symbol '%s' can not be at the same position in two productions with the same lhs:" % symbol, production_to_string(declaration))

                #     self.graph[lhs][symbol][str(i+1)] = rhs
            
        # self._grammar_graph.add_node('terminal', type='base')
        # self._grammar_graph.add_node('nonterminal', type='base')
        
        # self.__add_symbol = {
        #     True:self.__add_nonterminal,
        #     False:self.__add_terminal,
        #     }
        
        # for dec in declarations:
        #     self.__add_symbol[dec[0].islower()](*dec)

        # deriv = self.derivation_graph
        
        # axiom = [x for x in deriv.nodes if int(deriv.in_degree(x)) == 0]

        # axiom = [n for n in deriv.nodes() if not [x for x in deriv.predecessors(n) if x != n]]

        # print('AX', axiom)
        
        # self.__check_axiom(axiom)

        # self.__add_nonterminal('S', axiom[0])

        # deriv = nx.DiGraph(self.derivation_graph)
        # self.__check_unreachable_symbol(deriv)
        # self.__check_cycles(deriv)

    # @property
    # def grammar_graph(self):
    #     return self._grammar_graph
    
    # @property
    # def derivation_graph(self):
    #     edges = [(u,v) for u,v,data in self._grammar_graph.edges(data=True) if 'production' in data]
    #     return nx.DiGraph(self._grammar_graph.subgraph(nx.DiGraph(edges)))

    # @property
    # def type_graph(self):
    #     edges = [(u,v) for u,v,data in self._grammar_graph.edges(data=True) if 'type' in data]
    #     return nx.DiGraph(self._grammar_graph.subgraph(nx.DiGraph(edges)))
    
    # @property
    # def type_graph(self):
    #     return self._grammar_graph
    
    # @property
    # def terminals(self):
    #     return set(list(self.type_graph.predecessors('terminal')))
    
    # @property
    # def nonterminals(self):
    #     return set(list(self.type_graph.predecessors('nonterminal')))
    
    # @property
    # def axiom(self):
    #     return set(self._grammar_graph.successors('S'))

    # @property
    # def constants(self):
    #     return list(self.type_graph.predecessors('CONST'))

    
    # @property
    # def variables(self):
    #     return list(self.type_graph.predecessors('VAR'))
        
    # @property
    # def productions(self):
    #     grammar_prods = {}
        
    #     without_cycle = nx.DiGraph()
    #     for n, data in self._grammar_graph.nodes(data=True):
    #         if 'type' not in data.keys():
    #             print('###', n, data)
    #             without_cycle.add_path(list(nx.shortest_path(self._grammar_graph,'S',n)))


    #     print('HHH', set(self._grammar_graph))
    #     print('HHH', set(without_cycle))
    #     for n in list(nx.topological_sort(
    #         al.operators.intersection(
    #                 self.derivation_graph,
    #                 without_cycle))):


    #         print('NNNNNNNNN')
    #         if self.derivation_graph.out_degree(n):
    #             productions = sorted([p for successor in self.derivation_graph.successors(n)
    #                                             for p in self.derivation_graph[n][successor]['production']],
    #                                             key=len)

    #             prod = []
    #             for x in productions:
    #                 if x and x not in prod:
    #                     prod.append(x)

    #             grammar_prods[n] = []
    #             for p in prod:
    #                 grammar_prods[n].append(p[1:])

    #     print('RRR', grammar_prods)
    #     return grammar_prods

    # @staticmethod
    # def __check_axiom(axiom):
    #     if len(axiom) >1:
    #         raise Exception('a grammar can only have one axiom, found:', axiom)

    # @staticmethod
    # def __check_unreachable_symbol(graph):
    #     for n in graph.nodes:
    #         if not nx.has_path(graph, 'S', n):
    #             raise Exception('unreachable symbol %s' % n)

    # @staticmethod
    # def __check_cycles(graph):
    #     without_cycle = nx.DiGraph()
    #     for n in graph.nodes():
    #         without_cycle.add_path(nx.shortest_path(graph,'S',n))

    #     for cycle in al.cycles.simple_cycles(graph):
    #         if len(cycle) > 1:
    #             w = nx.DiGraph()
    #             longest = (0, None)
                
    #             for n in cycle:
    #                 path = nx.shortest_path(graph,'S', n)
    #                 w.add_path(path)
    #                 if len(path) > longest[0]:
    #                     longest = (len(path), n)

    #             diff = al.operators.difference(graph.subgraph(w.nodes), w)
    #             raise Exception('ambiguous context-free grammar, cycle found:  %s -> %s' % (
    #                 longest[1],
    #                 str([x for x in graph.successors(longest[1]) if x in w.nodes])
    #                 ))


    # @check_args(lambda *args: len(args) != 3, SyntaxError)
    # def __add_terminal(self, name, values, t_type):

    #     if isinstance(values, str):
    #         values = list(values)

    #     v_set = set(values)

    #     if len(values) != len(v_set):
    #         raise Exception('terminal values must be a set of unique object, duplicates found in %s := %s' % (name, str(values)))

    #     self._grammar_graph.add_node(name)

    #     if t_type not in self._grammar_graph:
    #         self._grammar_graph.add_node(t_type, type='base')

    #     values_str = '|'.join(str(x) for x in values)
    #     self._grammar_graph.add_edge(name, values_str, production=[(name, values_str)])
    #     self._grammar_graph.nodes[values_str]['values'] = set(values)
    #     self._grammar_graph.add_edge(values_str, t_type, type=t_type)
    #     self._grammar_graph.add_edge(name, t_type, type='terminal')
        
    #     # self._grammar_graph.nodes[values_str]['type'] = t_type

    # def __add_nonterminal(self, *declaration):
    #     lhs, rhs = declaration[0], declaration[1:]

    #     for symbol in rhs:
    #         if not self._grammar_graph.has_edge(lhs, symbol):
    #             self._grammar_graph.add_node(lhs)
    #             self._grammar_graph.add_edge(lhs, symbol, production=[declaration])
    #         else:
    #             if declaration not in self._grammar_graph[lhs][symbol]['production']:
    #                 self._grammar_graph[lhs][symbol]['production'].append(declaration)

            
    
    # def generate(self, max_recursion=-1):
    #     raise NotImplementedError()

    # def __repr__(self):
    #     prods_repr = [
    #         '# Grammar %s' % type(self),
    #         '# variables: %s' % repr(self.variables),
    #         '# constants: %s' % str(self.constants),
    #         '# productions:',
    #         ]

    #     for lhs, rhss in self.productions.items():
    #         print(lhs, rhss)
    #         prods_repr.append('%s := %s' % (lhs, ' '.join(rhss[0])))

    #         if len(rhss) > 1:
    #             for rhs in rhss[1:]:
    #                 prods_repr.append(' | %s' % ' '.join(rhs))

    #     return '\n'.join(prods_repr + ['#'])
