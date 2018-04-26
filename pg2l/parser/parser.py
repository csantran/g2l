# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from warnings import warn
from collections import UserList

import ply.yacc as yacc
import ply.lex as lex

from pg2l.grammar import Grammar

from .lexer import Lexer

class BaseModuleParser(object):
    G = None

    def __init__(self, lexer_module):
        super().__init__()
        self.tokens = lexer_module.tokens
        self.lexer = lex.lex(module=lexer_module)
        self.parser = yacc.yacc(
            module = self,
            start = self.G.axiom
            )

    @staticmethod
    def p_empty(p):
        'empty :'

    def p_error(self, p):
        if p:
            warn("Syntax error at token %s" % p.type)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()

        else:
            warn("Syntax error at EOF")

def ast_item_factory(terminals):
    def factory(args):
        name, value = args
        # print('NAME', name, value, terminals)
        return (value != None and name not in terminals) and type(name, (Item,), {})(value) or value

    return factory

class Item(UserList):
    def __repr__(self):
        return '(%s %s)' % (type(self).__name__, ','.join(repr(x) for x in self))

    def __str__(self):
        return '%s' % ''.join(str(x) for x in self if x)

def p_no_recursion(lhs, rhs, item_factory):
    lhs_cls = type(lhs, (Item,), {})

    def action(self, p):
        ast = map(item_factory , zip(rhs, p[1:]))
        p[0] = lhs_cls(ast)

    return action

def p_left_recursion(lhs, rhs, item_factory):
    lhs_cls = type(lhs, (Item,), {})

    def action(self, p):
        unpacked = [x for x in p[1] if x]
        p[0] = lhs_cls(unpacked)
        p[0] += map(item_factory, zip(rhs[1:], p[2:]))

    return action

def _build_parser_module_class(G):
    P = Grammar(G.subgraph(G.nonterminals))

    item_factory = ast_item_factory(P.terminals)

    clsdict = {'G':P}

    for lhs, rhs in P.productions:

        p_name = 'p_%s_%s' % (lhs, '_'.join(rhs))

        if lhs == rhs[0]:
            clsdict[p_name] = p_left_recursion(lhs, rhs, item_factory)
        else:
            clsdict[p_name] = p_no_recursion(lhs, rhs, item_factory)

    cls = type('ParserModule', (BaseModuleParser,), clsdict)

    for lhs, rhs in P.productions:
        p_doc_string = """%s : %s""" % (lhs, ' '.join(rhs))
        p_name = 'p_%s_%s' % (lhs, '_'.join(rhs))
        getattr(cls, p_name).__doc__ = p_doc_string

    return cls

class Parser(object):
    def __init__(self, G):
        ParserModule = _build_parser_module_class(G)
        lexer_module = Lexer(G)
        parser_module = ParserModule(lexer_module)
        self.parser = parser_module.parser

    def parse(self, string):
        return self.parser.parse(string)
