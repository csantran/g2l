# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from pg2l.base import AbstractGrammar
from pg2l.meta.parser.parser import Parser


class Grammar(AbstractGrammar):

    @staticmethod
    def from_string(self, meta, grammar):
        parser = Parser(meta)

        print(parser.parse(grammar))

    @staticmethod
    def from_declaration(self, meta, declarations):
        ...

    @staticmethod
    def from_generator(self, meta, seed):
        ...
