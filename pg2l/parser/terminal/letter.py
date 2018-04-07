# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import BaseLexer
from pg2l import grammar

@grammar.register('LETTER')
class LetterLexer(BaseLexer, grammar.Terminal):
    def __init__(self, letters):
        if not isinstance(letters, str):
            raise TypeError(letters)

        self.tokens += [grammar.Grammar.LETTER]
        self.variables += list(letters)

        self.t_LETTER = r'[%s]' % letters
