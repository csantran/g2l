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
from pg2l.grammar import Grammar as G

@register_with_nonterminal(G.node)
class NodeParser(ParserMixin):

    @staticmethod
    @docstring_production(str(ast.BaseNode.name), str(ast.Node.name))
    def p_basenode_node(p):
        """
        {0} : {1}
        """
        p[0] = p[1]

    @staticmethod
    @docstring_production(str(ast.Node.name), str(ast.Letter.name))
    def p_node(p):
        """
        {0} : {1}
        """
        p[0] = ast.Node()
        p[0].push(p[1])

    @staticmethod
    @docstring_production(str(ast.Letter.name), G.LETTER)
    def p_letter(p):
        """
        {0} : {1}
        """
        p[0] = ast.Letter(p[1])

@register_with_nonterminal(G.expression)
class ExpressionParser(ParserMixin):

    @staticmethod
    @docstring_production(G.expression, str(ast.Axiom.name))
    def p_expression_axiom(p):
        """
        {0} : {1}
        """
        p[0] = p[1]

    @staticmethod
    @docstring_production(str(ast.Axiom.name), str(ast.Level.name))
    def p_axiom_level(p):
        """
        {0} : {1}
        """
        p[0] = ast.Axiom()
        p[0].push(p[1])

    @staticmethod
    @docstring_production(str(ast.Level.name), str(ast.BaseNode.name))
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
