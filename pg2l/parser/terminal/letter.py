# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import LexerMixin, register_with_terminal

from pg2l import grammar
from pg2l.grammar import Grammar as G


@register_with_terminal(G.LETTER)
class LetterLexer(LexerMixin, grammar.Terminal):
    def __init__(self, letters):
        if not isinstance(letters, str):
            raise TypeError(letters)

        self.tokens += [G.LETTER]
        self.variables += list(letters)

        self.t_LETTER = r'[%s]' % letters
