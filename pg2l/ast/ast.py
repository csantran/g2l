# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
"""
NonTerminal Abstract Syntax Tree,
a tree of grammar nonterminals
"""
from .base import AbstractNonTerminalLeafSymbol, AbstractNonTerminalBranchSymbol, MetaSymbol
from .tree import Leaf
from .tree import BTree as Infix
from .tree import BTreeLeft as LeftOperand
from .tree import BTreeRight as RightOperand
from .tree import KTree as Container
from .tree import BaseTree


# *********
# NonTerminalLeaf
# *********

# leafs of NonTerminal AST
class Expression(AbstractNonTerminalBranchSymbol, metaclass=MetaSymbol):
    """EXpression"""

class NonTerminalLeaf(AbstractNonTerminalLeafSymbol, Leaf):
    """nonterminal leaf object, a string"""

class Label(NonTerminalLeaf, LeftOperand, metaclass=MetaSymbol):
    """A letter"""

class Empty(Label, metaclass=MetaSymbol):
    """The empty symbol"""

    def __init__(self):
        super().__init__('')

    def __repr__(self):
        return '(%s)' % Empty.symbol

class Jump(NonTerminalLeaf, metaclass=MetaSymbol):
    """A Jump, a string that represent a number"""

# ************
# NonterminalBranch
# ************
#
# branchs of Nonterminal ast

class NonTerminalBranch(AbstractNonTerminalBranchSymbol):
    """branchs"""
    def __str__(self):
        """String representation of a tree

        Returns
        -------
        str
            string representation of a tree and all its children recursively
        """
        return ''.join(str(x) for x in self.children)

class BaseNode(NonTerminalBranch, Infix, metaclass=MetaSymbol):
    """Node base class, contains symbols"""

class Node(BaseNode, metaclass=MetaSymbol):
    """An node with only a letter symbol on his left side"""

class JNode(Node, metaclass=MetaSymbol):
    """An node with a letter symbol on the left and a round of jump symbols on his right side"""

class Module(BaseNode, metaclass=MetaSymbol):
    """An module with only a level (a level is also a symbol) on his left side"""
    def __str__(self):
        """String representation of a module"""
        return '[%s]' % super().__str__()

class JModule(Module, metaclass=MetaSymbol):
    """An module with a level on the left and a round of jump on the right side"""

    def __str__(self):
        """String representation of a connected module"""
        return '[%s]%s' % (self.left, self.right)

class Level(NonTerminalBranch, Container, LeftOperand, metaclass=MetaSymbol):
    """A level,
    container for atoms, that is, it contains the nodes and modules of the same level"""
    pass

class Round(NonTerminalBranch, Container, RightOperand, metaclass=MetaSymbol):
    """A round,
    container for jumps"""
    pass

# ******
# String
# ******

class String(NonTerminalBranch, Container):
    """A string, a word of the language, a set of atoms
    """
    pass

class Axiom(String, metaclass=MetaSymbol):
    """An axiom"""
    pass

# ****************
# Production rules
# ****************

class Predecessor(String, LeftOperand):
    """Predecessor,
    left part of a rewriting rule"""
    pass

class Successor(String, RightOperand):
    """Predecessor,
    right part of a rewriting rule"""
    pass

class Rule(Infix, LeftOperand):
    """Rule,
    the rewriting rule composed of the predecessor on the left
    and the successor on the right
    """
    @property
    def predecessor(self):
        """predecessor getter"""
        return self.left

    @property
    def successor(self):
        """successor getter"""
        return self.right

# *******
# Context
# *******

class Contexts(NonTerminalBranch, Container, RightOperand):
    """Context of a production rule,
    contains context strings"""
    pass

class ContextString(String):
    """Context string base classe"""
    pass

class GraphLeftContext(ContextString):
    """Left-context seen from the point of view of the graph representation"""
    pass

class GraphRightContext(ContextString):
    """Right-context seen from the point of view of the graph representation"""
    pass

class StringLeftContext(ContextString):
    """Left-context seen from the point of view of the string representation"""
    pass

class StringRightContext(ContextString):
    """Right-context seen from the point of view of the string representation"""
    pass

class BaseProduction(Infix):
    """Production rule base class,
    contains a rewriting rule on his left side
    """
    @property
    def rule(self):
        """rule getter"""
        return self.left

class Production(BaseProduction, metaclass=MetaSymbol):
    """Production"""

class Identity(BaseProduction):
    """Identity production where the successor is identical to the predecessor"""

class G0L(BaseProduction):
    """G0L,
    a context-free production rule"""

    def __str__(self):
        """String representation of a context-free production"""
        return '%s:%s' % (str(self.children[0]), str(self.children[1]))

class G1LL(BaseProduction):
    """G1LL,
    a non context-free production rule with left-context"""

    @property
    def left(self):
        """left context getter"""
        return self.children[2]

    def __str__(self):
        """String representation of a G1LL production"""
        return '%s<%s:%s' % (str(self.children[2]), str(self.children[0]), str(self.children[1]))

class G1LR(BaseProduction):
    """G1LR
    a non context-free production rule with right-context"""

    @property
    def right(self):
        """right context getter"""
        return self.children[2]

    def __str__(self):
        """String representation of a G1LR production"""
        return '%s>%s:%s' % (str(self.children[0]), str(self.children[2]), str(self.children[1]))

class G2L(BaseProduction):
    """G2L,
    a non context-free production rule with both left and right context"""

    @property
    def left(self):
        """left context getter"""
        return self.children[2]

    @property
    def right(self):
        """right context getter"""
        return self.children[3]

    def __str__(self):
        """String representation of a G2LR production"""
        return '%s<%s>%s:%s' % (str(self.children[2]),
                                str(self.children[0]),
                                str(self.children[3]),
                                str(self.children[1]))

# class REWRITE(Leaf):
#     """operator TO"""
#     pass

# class LEFT(Leaf):
#     """operator left context"""
#     pass

# class RIGHT(Leaf):
#     """operator right context"""
#     pass

def copy(obj):
    """Do a shallow copy of tree

    Examples
    --------
    >>> x = Label('B')
    >>> y = copy(x)
    >>> print(y)
    B
    >>> print(repr(y))
    (label B)

    Parameters
    ----------
    tree: :obj:`tree`
       a tree

    Returns
    -------
    :obj:`tree`
        orphaned shallow copy of a tree
    """
    t_copy = isinstance(obj, NonTerminalLeaf) and type(obj)(str(obj)) or type(obj)()

    if isinstance(obj, BaseTree):
        for child in obj.children:
            t_copy.push(copy(child))

    return t_copy
