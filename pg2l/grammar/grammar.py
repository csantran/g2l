# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
import types

import networkx as nx


class Grammar(nx.DiGraph):

    @property
    def axiom(self):
        inputs = [n for n in self.nodes() if not
                     [p for p in self.predecessors(n) if p != n]]

        return inputs[0] if len(inputs) == 1 else None

    @property
    def terminals(self):
        return set([n for n in self.nodes() if
                            self.out_degree(n) == 0 and n != 'empty'])

    @property
    def nonterminals(self):
        return self.alphabet - self.terminals

    @property
    def alphabet(self):
        return set(self.nodes())

    @property
    def productions(self):
        productions = {}

        for u,_,data in self.edges(data=True):

            if u not in productions:
                productions[u] = []
                
            for prod in data['production']:
                prod_hash = ''.join(str(x) for x in prod)

                if prod_hash not in productions[u]:
                    productions[u].append(prod_hash)
                    yield (u, prod)

    def __add__(self, grammar):
        return Grammar(nx.compose(self, grammar))

def add_production(graph, declaration):
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
        add_production(G, declaration)

    return G

# def grammar_relabel_to_integer(G):
#     without_cycle = nx.DiGraph()
#     for n, data in G.graph.nodes(data=True):
#         without_cycle.add_path(list(nx.shortest_path(G.graph,G.axiom,n)))

#     g2h_mapping = {n:i+1 for i,n in enumerate(nx.topological_sort(without_cycle))
#                        if n not in ('ε', '$')}

#     g2h_mapping["$"] = 0

#     if 'ε' in without_cycle:
#         g2h_mapping['ε'] = -1

#     H = nx.relabel.relabel_nodes(G.graph, mapping=g2h_mapping, copy=False)

#     h2g_mapping = {v:k for k,v in g2h_mapping.items()}

#     for n in list(H.nodes()):
#         H.nodes[n]['symbol'] = h2g_mapping[n]

#     for u,v,data in H.edges(data=True):
#         H[u][v]['production'] = [[g2h_mapping[x] for x in prod]
#                                      for prod in H[u][v]['production']]

#     return Grammar(H), (g2h_mapping, h2g_mapping)
