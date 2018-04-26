# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
import re
from warnings import warn

from pg2l.grammar import Grammar


class Lexer(object):
    def __init__(self, G):
        super().__init__()
        self.tokens = []

        lex_nodes = []
        for u,v in G.edges():
            if v in G.terminals:
                lex_nodes += [u,v]

        L = Grammar(G.subgraph(list(set(lex_nodes))))

        for nterm in L.nonterminals:
            self.tokens.append(nterm)

            if L.out_degree(nterm) == 1:
                constant = list(L.successors(nterm))[0]
                setattr(self, 't_%s' % nterm, '%s' % re.escape(constant))

            else:
                values = list(L.successors(nterm))
                setattr(self, 't_%s' % nterm, r'|'.join(['%s' % i for i in values]))

    @staticmethod
    def t_error(t):
        warn("illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
