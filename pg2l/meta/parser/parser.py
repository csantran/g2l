# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from warnings import warn

import ply.yacc as yacc
import ply.lex as lex

from pg2l.meta.grammar import MetaGrammar, GrammarItem

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
        return (value != None and name not in terminals) and type(name, (GrammarItem,), {})(value) or value

    return factory

def p_no_recursion(lhs, rhs, item_factory):
    lhs_cls = type(lhs, (GrammarItem,), {})

    def action(self, p):
        ast = map(item_factory , zip(rhs, p[1:]))
        p[0] = lhs_cls(ast)

    return action

def p_left_recursion(lhs, rhs, item_factory):
    lhs_cls = type(lhs, (GrammarItem,), {})

    def action(self, p):
        unpacked = [x for x in p[1] if x]
        p[0] = lhs_cls(unpacked)
        p[0] += map(item_factory, zip(rhs[1:], p[2:]))

    return action

def p_right_recursion(lhs, rhs, item_factory):
    lhs_cls = type(lhs, (GrammarItem,), {})

    def action(self, p):
        last = len(p) -1
        unpacked = [x for x in p[last] if x]
        p[0] = lhs_cls(map(item_factory, zip(rhs[0:-1], p[1:last])))
        p[0] += unpacked

    return action

def _build_parser_module_class(G):
    P = MetaGrammar(G.subgraph(G.nonterminals))

    item_factory = ast_item_factory(P.terminals)

    clsdict = {'G':P}

    for lhs, rhs in P.productions:

        p_name = 'p_%s_%s' % (lhs, '_'.join(rhs))

        if lhs == rhs[0]:
            clsdict[p_name] = p_left_recursion(lhs, rhs, item_factory)
        elif lhs == rhs[-1]:
            clsdict[p_name] = p_right_recursion(lhs, rhs, item_factory)
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
        self.lexer_module = Lexer(G)
        self.parser_module = ParserModule(self.lexer_module)
        self.parser = self.parser_module.parser

    def parse(self, string):
        return self.parser.parse(string)
