# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
"""
Base classes for ast.
Contain :obj:`Leaf`, :obj:`BaseTree`, :obj:`KTree` and :obj:`BTree`
"""
from abc import ABC, abstractmethod
from collections import OrderedDict


class Leaf(object):
    repr_string = '(LEAF %s)'

    def __init__(self):
        super().__init__()
        self.parent = None

    # def __repr__(self):
    #     """Representation of leaf

    #     Returns
    #     -------
    #     str
    #         string representation of leaf

    #     """
    #     return self.repr_string % str(self)

    # def __str__(self):
    #     """String representation of leaf

    #     Returns
    #     -------
    #     str
    #         string representation of leaf data's
    #     """
    #     return str(self)

    def __iter__(self):
        yield self


class BaseTree(ABC, Leaf):
    """Base class for non terminals
    """
    @property
    @abstractmethod
    def children(self):
        """Property getter for tree children's, abstract method implemented in sub classes
        """
        raise NotImplementedError()

    @abstractmethod
    def push(self, child):
        """Push children into the tree, abstract method implemented in sub classes
        """
        raise NotImplementedError()

    # def __str__(self):
    #     """String representation of a tree

    #     Returns
    #     -------
    #     str
    #         string representation of a tree and all its children recursively
    #     """
    #     return ''.join(str(x) for x in self.children)

    def __iter__(self):
        """Iterator over the tree,
        deep first pre-order traversal of a tree

        Yields
        ------
        :obj:`Leaf`
            all nodes of a tree in deep first pre-order
        """
        yield self
        for child in self.children:
            if child:
                yield from child

class KTree(BaseTree):
    """
    A simple k-ary tree

    """
    repr_string = '(KTREE %s)'

    def __init__(self):
        super().__init__()
        self.__children = []

    @property
    def children(self):
        """Property getter for tree children's
        Returns
        -------
        :obj:`tuple`
           tuple of tree direct children
        """
        return tuple(self.__children)

    def push(self, child):
        """Push child into parent children list's

        Insert child in tree, child is appended to the end of tree instance children list's.

        Parameters
        ----------
        child : :obj:`Leaf`
            a Leaf instance

        Raises
        ------
        AssertionError
           if child is not orphaned and its parent is not set to None
        TypeError
           if child is not a :obj:`Leaf` instance
        """
        if not isinstance(child, Leaf):
            raise TypeError('child wrong type %s, try to push it in %s' % (child, self))

        if child.parent is not None:
            raise AssertionError('child %s is not orphaned, parent %s' % (child, child.parent))

        child.parent = self
        self.__children.append(child)

class BTreeLeft(object):
    """Base class for left object in a :obj:`BTree`"""
    pass

class BTreeRight(object):
    """Base class for right object in a :obj:`BTree`"""
    pass

class BTree(BaseTree):
    """
    A simple binary tree
    """
    LEFT = 'left'
    RIGHT = 'right'
    _map_side = {
        LEFT:  BTreeLeft,
        RIGHT: BTreeRight,
        }

    repr_string = '(BTREE %s)'

    def __init__(self):
        super().__init__()
        self.__children = OrderedDict((x, None) for x in (BTree.LEFT, BTree.RIGHT))

    @property
    def children(self):
        """Property getter for tree children's
        Returns
        -------
        :obj:`tuple`
           tuple of tree direct children
        """
        return tuple(x for x in self.__children.values() if x)

    @property
    def left(self):
        """Property getter for tree left child
        Returns
        -------
        :obj:`Leaf`
           left child
        """
        return self.__children[BTree.LEFT]

    @property
    def right(self):
        """Property getter for tree right child
        Returns
        -------
        :obj:`Leaf`
           right child
        """
        return self.__children[BTree.RIGHT]

    def push(self, child):
        """Push child into parent children list's

        Insert child in tree, child is appended to the end of tree instance children list's.

        Parameters
        ----------
        child : :obj:`Leaf`
            a child, must be a :obj:`Leaf` or a :obj:`KTree` instance
            and a sub class of :obj:`BTreeLeft` or :obj:`BTreeRight`

        Raises
        ------
        AssertionError
           if child is not orphaned and its parent is not set to None
        TypeError
           if child is not a :obj:`Leaf` or a :obj:`KTree` instance
        AttributeError
           if tree have already a child
        """
        if isinstance(child, BTree) \
          or not isinstance(child, (Leaf, KTree)) \
          or not isinstance(child, (BTreeLeft, BTreeRight)):
            raise TypeError('child wrong type %s, try to push it in %s' % (child, self))

        if child.parent is not None:
            raise AssertionError('child %s is not orphaned, parent %s' % (child, child.parent))

        side = isinstance(child, BTreeLeft) and BTree.LEFT or BTree.RIGHT
        if self.__children[side] is not None:
            raise AttributeError('child already exists %s' % self.__children[side])

        child.parent = self
        self.__children[side] = child

