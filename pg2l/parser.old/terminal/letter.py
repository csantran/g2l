# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import LexerMixin, register_with_terminal

from pg2l.ast import MetaDeclaration as G


@register_with_terminal(G.LETTER.symbol)
class LetterLexer(LexerMixin):
    def __init__(self, letters):
        if not isinstance(letters, str):
            raise TypeError(letters)

        self.tokens += [G.LETTER.symbol]
        self.variables += list(letters)

        setattr(LetterLexer, 't_%s' % G.LETTER.symbol, staticmethod(lambda x: x))
        getattr(LetterLexer, 't_%s' % G.LETTER.symbol).__doc__ = r'|'.join(['%s' % i for i in letters])