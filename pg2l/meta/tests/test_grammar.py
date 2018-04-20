# -*- coding : utf-8 -*-
from collections import defaultdict
from functools import reduce
import unittest

# from pg2l.ast.base import AbstractTerminalSymbol
# from pg2l.ast.base import MetaSymbol
# from pg2l.meta.declaration import MetaDeclaration as G

# class TestMetaDeclaration(unittest.TestCase):

#     def test_terminal_leaf(self):
#         class Op_Rewrite(AbstractTerminalSymbol, metaclass=MetaSymbol):
#             pass

#         self.assertEqual(Op_Rewrite.name, 'OP_REWRITE')
#         self.assertEqual(G.OP_REWRITE, Op_Rewrite)
import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
# import tempfile
# import tkinter as tk

from pg2l.meta import declaration as G
from pg2l.meta.grammar import Grammar, build

class TestMetaGrammar(unittest.TestCase):

    def test_meta_grammar(self):

        meta = build(
            ('LETTER', list('AB')),
            ('NUMBER', range(3)),
            ('LBR', '['),
            ('RBR', ']'),
            ('string', 'node', 'string'),
            ('string', 'esubstring', 'string'),
            ('string', 'ε'),
            ('node', 'LETTER', 'jump'),
            ('jump', 'NUMBER', 'jump'),
            ('jump', 'ε'),
            ('esubstring', 'LBR', 'RBR'),
            # ('string', 'substring', 'string'),
            # ('substring', 'LBR', 'string', 'RBR'),
            )

        meta = build( 
            ('S', 'F'),
            ('S', '(', 'S', '+', 'F', ')'),
            ('F', '1'),
            )
        print()
        print('AX', meta.axiom)
        print('TERM', meta.terminals)
        
        A = to_agraph(meta.graph)
        A.layout('dot')
        A.draw('meta.png')

        
        def grammar_to_parser(grammar):
            parser = build(("S'", grammar.axiom, "$"),) + grammar

            without_cycle = nx.DiGraph()
            for n, data in parser.graph.nodes(data=True):
                without_cycle.add_path(list(nx.shortest_path(parser.graph,parser.axiom,n)))

            mapping = {n:i+1 for i,n in enumerate(nx.topological_sort(without_cycle))
                           if n not in ('ε', '$')}

            mapping["$"] = 0
            
            if 'ε' in without_cycle:
                mapping['ε'] = -1

            mapped = nx.relabel.relabel_nodes(parser.graph, mapping=mapping, copy=False)
            mapping_rev = {v:k for k,v in mapping.items()}

            for n in list(mapped.nodes()):
                mapped.nodes[n]['symbol'] = mapping_rev[n]
                
            for u,v,data in mapped.edges(data=True):
                mapped[u][v]['production'] = [[mapping[x] for x in prod]
                                             for prod in mapped[u][v]['production']]

            return Grammar(mapped)

        def _first(grammar, α):
            if not grammar.graph.out_degree(α) and grammar.graph.nodes[α]['symbol'] != -1:
                yield α
            else:
                for aβ in grammar.graph.successors(α):
                    for a, *_ in grammar.graph[α][aβ]['production']:
                        yield from _first(grammar, a)
                
        def first(grammar, α):
            return set(_first(grammar, α))

        def epsilon(grammar, α):
            return -1 in grammar.graph and α in grammar.graph.predecessors(-1)

        def _follow(grammar, α):
            for u,s,data in grammar.graph.edges(data=True):
                
                for βαγ in data['production']:
                    if α in βαγ:
                        αi = βαγ.index(α)
                        γ = len(βαγ) > αi+1 and βαγ[αi+1] or None

                        if γ:
                            yield from _first(grammar, γ)
                        elif α != -1:
                            yield 0

        def follow(grammar, α):
            return set(_follow(grammar, α))
        
        A = grammar_to_parser(meta)

        d = to_agraph(A.graph)
        d.layout('dot')
        d.draw('parser.png')

        print('alphabet', A.alphabet)
        print('nonterminals', A.alphabet - A.terminals)
        print('\nPROD', list(grammar_to_parser(meta).productions))

        # memoize
        FIRST = {α:first(A,α) for α in A.alphabet}
        EPSILON = {α:epsilon(A,α) for α in A.alphabet}
        FOLLOW = {α:follow(A,α) for α in A.alphabet}
        
        print()
        print('first table')
        for k,v in FIRST.items():
            print(k,v)

        print()
        print('epsilon table')
        for k,v in EPSILON.items():
            print(k,v)

        table = {}

        for symbol in A.nonterminals:
            for succ in A.graph.successors(symbol):
                if symbol not in table:
                    table[symbol] = {}

                for prod in A.graph[symbol][succ]['production']:
                    for a in first(A, prod[0]):
                        if a not in table[symbol]:
                            table[symbol][a] = []
                        
                        table[symbol][a].append((symbol, prod))

                    if epsilon(A, prod[0]):
                        print('EPSILON', prod[0], first(A, prod[0]))
                        
                        # for b in follow(A, prod[0]):
                        #     if b not in table[symbol]:
                        #         table[symbol][b] = []
                        #     table[symbol][b].append((symbol, prod))
                
        mapping = {data['symbol']:n for n,data in A.graph.nodes(data=True)}
        mapping_rev = {v:k for k,v in mapping.items()}

        print()
        print('follow table')
        for k,v in FOLLOW.items():
            print(mapping_rev[k],[mapping_rev[x] for x in v])
        print()

        for nonterminal, terminals in table.items():
            print(mapping_rev[nonterminal])

            
            for terminal, productions in terminals.items():
                lhs, rhs = zip(*productions)

                if len(list(set(lhs))) != 1:
                    print('rr', lhs, rhs)
                    raise Exception('first/first conflict 1')
                
                if len(productions) >1:
                    _, result = reduce(
                        lambda res,pj:(pj, res[1] and (res[0]==pj)),
                        productions[1:],
                        (productions[0],True)
                        )
                    if not result:
                        raise Exception()

                table[nonterminal][terminal] = productions[0]
                print('\t', mapping_rev[terminal], ':', mapping_rev[table[nonterminal][terminal][0]], '->', [mapping_rev[x] for x in table[nonterminal][terminal][1]])
                
        input = [mapping[x] for x in '(1+1)'] + [mapping['$']]
        stack = [A.axiom]

        i = 0
        while len(input):
            token = input[0]
            print('\nclock', i)
            print(r'token {%s} ,%s' % (mapping_rev[token], ','.join([mapping_rev[x] for x in input[1:]])))
            print(r'stack {%s} ,%s' % (mapping_rev[stack[0]], ','.join([mapping_rev[x] for x in stack[1:]])))

            if token:
                if not(stack[0]):
                    raise Exception()

                if stack[0] in A.nonterminals:
                    if not (token in table[stack[0]]):
                        raise Exception('table lookup error')
                        
                    print('#  %s -> %s' % (mapping_rev[table[stack[0]][token][0]],
                                                        str([mapping_rev[x] for x in table[stack[0]][token][1]])))
                    poped = stack.pop(0)
                    stack = table[poped][token][1] + stack

                elif stack[0] in A.terminals:
                    if not (stack[0] == token):
                        raise Exception()

                    print('is terminal')
                    input.pop(0)
                    stack.pop(0)
                        
                else:
                    raise Exception()
                
            elif stack[0]:
                raise Exception()
                
            else:
                break
                    
            i += 1
            
        print('\nclock', i)
        print(r'token {%s} ,%s' % (mapping_rev[token], ','.join([mapping_rev[x] for x in input[1:]])))
        print(r'stack {%s} ,%s' % (mapping_rev[stack[0]], ','.join([mapping_rev[x] for x in stack[1:]])))


        

if __name__ == '__main__':
    unittest.main(verbosity=2)
