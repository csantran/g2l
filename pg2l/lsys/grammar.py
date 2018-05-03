# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from pg2l.meta.parser.parser import Parser

import networkx as nx

class Grammar(nx.DiGraph):

    @staticmethod
    def from_string(meta, grammar):
        parser = Parser(meta)

        expression = parser.parse(grammar)

        if expression:
            if type(expression[0]).__name__ == 'grammar':
                print('axiom', expression[0][0])
                for p in expression[0][2]:
                    if type(p).__name__ == 'production':
                        print('production', p)
            else:
                raise Exception()
        else:
            raise Exception()


    @staticmethod
    def from_declaration(meta, declarations):
        pass

    @staticmethod
    def from_generator(self, meta, seed):
        pass
