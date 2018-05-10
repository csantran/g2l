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

from pg2l.meta.grammar import MetaGrammar


class Lexer(object):
    def __init__(self, G):
        super().__init__()
        self.tokens = []

        lex_nodes = []
        for u,v in G.edges():
            if v in G.terminals:
                if v == 'NEWLINE':
                    if 'NEWLINE' not in self.tokens:
                        def t_NEWLINE(t):
                            r'\n+'
                            t.lexer.lineno += len(t.value)
                            return t

                        setattr(self, 't_NEWLINE', t_NEWLINE)
                        self.tokens.append('NEWLINE')

                else:
                    lex_nodes += [u,v]

        L = MetaGrammar(G.subgraph(list(set(lex_nodes))))

        for nterm in L.nonterminals:
            self.tokens.append(nterm)

            if L.out_degree(nterm) == 1:

                constant = list(L.successors(nterm))[0]

                if isinstance(constant, str):
                    setattr(self, 't_%s' % nterm, '%s' % re.escape(constant))
                elif isinstance(constant, re._pattern_type):
                    setattr(self, 't_%s' % nterm, constant.pattern)
                else:
                    raise Exception()

            else:
                values = list(L.successors(nterm))
                setattr(self, 't_%s' % nterm, r'|'.join(['%s' % i for i in values]))

        self.L = L

    @staticmethod
    def t_error(t):
        warn("illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
