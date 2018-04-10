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
from .base import AbstractNonTerminal
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

class NonTerminalLeaf(AbstractNonTerminal, Leaf):
    """
    A simple leaf object that contains value

    Parameters
    ----------
    value : dict
        terminal data's
    """
    _value = None

    def __init__(self, value=''):
        super().__init__()
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self.value

class Letter(NonTerminalLeaf, LeftOperand):
    """A letter"""
    pass

class Empty(Letter):
    """The empty symbol"""
    pass

class Jump(NonTerminalLeaf):
    """A Jump, a number"""

    def __str__(self):
        return str(self.value)

# ************
# NonterminalBranch
# ************
#
# branchs of Nonterminal ast 

class NonTerminalBranch(AbstractNonTerminal):
    """branchs"""
    def __str__(self):
        """String representation of a tree

        Returns
        -------
        str
            string representation of a tree and all its children recursively
        """
        return ''.join(str(x) for x in self.children)

class BaseNode(NonTerminalBranch, Infix):
    """Node base class, contains symbols"""
    pass

class Node(BaseNode):
    """An node with only a letter symbol on his left side"""
    pass

class JNode(Node):
    """An node with a letter symbol on the left and a round of jump symbols on his right side"""
    pass

class Module(BaseNode):
    """An module with only a level (a level is also a symbol) on his left side"""
    def __str__(self):
        """String representation of a module"""
        return '[%s]' % super().__str__()

class JModule(Module):
    """An module with a level on the left and a round of jump on the right side"""

    def __str__(self):
        """String representation of a connected module"""
        return '[%s]%s' % (self.left, self.right)

class Level(NonTerminalBranch, Container, LeftOperand):
    """A level,
    container for atoms, that is, it contains the nodes and modules of the same level"""
    pass

class Round(NonTerminalBranch, Container, RightOperand):
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

class Axiom(String):
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

class Identity(BaseProduction):
    """Identity production where the successor is identical to the predecessor"""
    def __init__(self, predecessor):
        raise NotImplementedError()

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
    >>> x = Letter('B')
    >>> y = copy(x)
    >>> print(y.value)
    B
    >>> print(str(y))
    B
    >>> print(repr(y))
    (letter B)

    Parameters
    ----------
    tree: :obj:`tree`
       a tree

    Returns
    -------
    :obj:`tree`
        orphaned shallow copy of a tree
    """
    t_copy = isinstance(obj, NonTerminalLeaf) and type(obj)(obj.value) or type(obj)()

    if isinstance(obj, BaseTree):
        for child in obj.children:
            t_copy.push(copy(child))

    return t_copy
