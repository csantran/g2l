# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import ParserMixin, docstring_production, register_with_nonterminal

from pg2l.ast import terminals
from pg2l.ast import Grammar as G


@register_with_nonterminal(G.node.name)
class NodeParser(ParserMixin):

    @staticmethod
    @docstring_production(G.basenode, G.node)
    def p_basenode_node(p):
        """
        {0} : {1}
        """
        p[0] = p[1]

    @staticmethod
    @docstring_production(G.node, G.label)
    def p_node(p):
        """
        {0} : {1}
        """
        print('LLL', type(p[1]))
        p[0] = G.node()
        p[0].push(p[1])

    @staticmethod
    @docstring_production(G.label, G.LETTER)
    def p_letter(p):
        """
        {0} : {1}
        """
        print('TTT', type(p[1]))
        p[0] = G.label(G.LETTER(p[1]))

@register_with_nonterminal(G.expression.name)
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
        p[0] = G.axiom()
        p[0].push(p[1])

    @staticmethod
    @docstring_production(G.level, G.basenode)
    def p_level_basenode(p):
        """
        {0} : {1}
            | {0} {1}
        """
        if len(p) == 2:
            p[0] = G.level()
            p[0].push(p[1])

        elif len(p) == 3:
            p[0] = p[1]
            p[0].push(p[2])
