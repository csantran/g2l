# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>

import networkx as nx

def apt_dft(apt):

    for matching_symbol in apt:
        if type(matching_symbol).__name__ in ('symbol', 'level', 'string', 'substring'):
            yield matching_symbol

        if type(matching_symbol).__name__ in ('level', 'string', 'substring'):
            yield from apt_dft(matching_symbol)

def asg_add_string_edges(S, mapping, expression):
    last = None

    for matching_symbol in expression:
        if type(matching_symbol).__name__ in ('symbol', 'level'):
            if last:
                S.add_edge(mapping[id(last)], mapping[id(matching_symbol)], type='string_forward')
                S.add_edge(mapping[id(matching_symbol)], mapping[id(last)], type='string_backward')

            last = matching_symbol

        if type(matching_symbol).__name__ in ('level', 'string', 'substring'):
            for sub_symbol in matching_symbol:
                if type(sub_symbol).__name__ in ('symbol', 'level', 'string', 'substring'):
                    S.add_edge(mapping[id(matching_symbol)], mapping[id(sub_symbol)], type='sub')

            asg_add_string_edges(S, mapping, matching_symbol)

def constant_value(value):
    def _get_value():
        return value

    return _get_value

def dynamic_value(ASG, i):
    def _get_value():
        return

    return _get_value

def apt_to_asg(apt):
    ASG = nx.DiGraph()

    mapping = {}
    for i, matching_sym in enumerate(apt_dft(apt)):
        print('matching_sym', i, str(matching_sym), type(matching_sym).__name__)
        name = type(matching_sym).__name__
        value_getter = None

        if name in ('string', 'substring', 'level'):
            value_getter = dynamic_value(ASG, i)
        else:
            value_getter = constant_value(str(matching_sym))

        ASG.add_node(i, value=value_getter, type=name)
        mapping[id(matching_sym)] = i

    asg_add_string_edges(ASG, mapping, apt)

    for n, data in ASG.nodes(data=True):
        if data['type'] == 'substring':
            subgraph = ASG.subgraph(ASG.successors(n))
            print('succ', list(subgraph.edges(data=True)))
            forward_edges = [(u,v) for u,v,data in subgraph.edges(data=True) if data['type'] == 'string_forward']

            substring = nx.DiGraph()
            substring.add_edges_from(forward_edges)

            print('forward_edges', forward_edges)
            print('start', [x for x in substring.nodes() if substring.in_degree(x) == 0])
            print('end', [x for x in substring.nodes() if substring.out_degree(x) == 0])

    return ASG
