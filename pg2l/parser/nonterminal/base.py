# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from inspect import ismethod, getmro
import ply.yacc as yacc

from pg2l.parser.base import decorator_register_factory
from pg2l.parser.mixin import AbstractMixin
from pg2l.ast import Grammar as G

class ParserMixin(AbstractMixin):
    """Parser Mixin base class"""

def get_class_that_defined(method):
    for cls in getmro(method.__self__.__class__)[1:]:
        if cls.__dict__.get(method.__name__):
            return cls

class BaseParser(ParserMixin):
    def __init__(self, debug=False, strict=False):
        self.lexer = None
        self.tokens = None
        self.parser = None
        self.__strict = strict
        self.__debug = debug

    def parse(self, string):
        return self.parser.parse(string)

    def p_error(self, p):
        if p:
            if self.__strict:
                raise SyntaxError("Syntax error at token %s" % p.type)
            print("Syntax error at token", p.type)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()

        else:
            if self.__strict:
                raise EOFError("Syntax error at EOF")

            print("Syntax error at EOF")

    def __repr__(self):
        repr_string = []

        for name in dir(self):
            if name.startswith('p_') and name not in ('p_error', '__init__'):
                method = getattr(self, name)
                if ismethod(method):
                    repr_string.append('\n#from %s.%s' % (
                        get_class_that_defined(method),
                        method.__name__))
                else:
                    repr_string.append('\n#from %s' % method.__name__)

                for line in [l.strip() for l in method.__doc__.split('\n')]:
                    if line:

                        repr_string.append((line.startswith('|') and '\t%s' or '%s') % line)

        return '\n'.join(repr_string)

    def build(self, lexer):
        self.lexer = lexer
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module = self,
                                start = G.expression.name,
                                tabmodule = "baseparsetab",
                                outputdir = ".",
                                debug = self.__debug)
        return self

def docstring_production(*args):
    def __decorate(method):
        method.__doc__ = method.__doc__.format(*[x.name for x in args])
        return method

    return __decorate

nonterminals = {}

register_with_nonterminal = decorator_register_factory(nonterminals)
