# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import ParserMixin, docstring_production, register_with_nonterminal

from pg2l import ast
from pg2l import grammar
from pg2l.grammar import Grammar as G

grammar.register('basenode', 'node', 'letter')()

@register_with_nonterminal(G.node)
class NodeParser(ParserMixin):

    @staticmethod
    @docstring_production(G.basenode, G.node)
    def p_basenode_node(p):
        """
        {0} : {1}
        """
        p[0] = p[1]

    @staticmethod
    @docstring_production(G.node, G.letter)
    def p_node(p):
        """
        {0} : {1}
        """
        p[0] = ast.Node()
        p[0].push(p[1])

    @staticmethod
    @docstring_production(G.letter, G.LETTER)
    def p_letter(p):
        """
        {0} : {1}
        """
        p[0] = ast.Letter(symbol=p[1])

grammar.register('expression', 'axiom', 'level')()

@register_with_nonterminal(G.expression)
class ExpressionParser(ParserMixin):

    @staticmethod
    @docstring_production(G.expression, G.axiom)
    def p_expression_axiom(p):
        """
        {0} : {1}
        """
        p[0] = p[1]

    @staticmethod
    @docstring_production(G.axiom, G.level)
    def p_axiom_level(p):
        """
        {0} : {1}
        """
        p[0] = ast.Axiom()
        p[0].push(p[1])

    @staticmethod
    @docstring_production(G.level, G.basenode)
    def p_level_basenode(p):
        """
        {0} : {1}
            | {0} {1}
        """
        if len(p) == 2:
            p[0] = ast.Level()
            p[0].push(p[1])

        elif len(p) == 3:
            p[0] = p[1]
            p[0].push(p[2])
