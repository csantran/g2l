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
Contain :obj:`Leaf`, :obj:`BaseTree`, :obj:`Ktree` and :obj:`Btree`
"""
from abc import ABC, abstractmethod
from collections import OrderedDict


class Leaf(object):
    """
    A simple terminal object that contains data
    
    Parameters
    ----------
    data : \*\*dict
        leaf data's in an unpacked :obj:`dict` or :obj:`list` of :obj:`(key,value)` pairs
            
    Attributes
    ----------

    repr_string : formated string
        class attribut, a formated string used by __repr__, '%s' is then replaced by the value returned by __str__

    data : dict
        the data dictionary of the leaf

    parent : :obj:`BaseTree`
        None if leaf is orphaned otherwise a BaseTree object

    Examples
    --------
    A simple symbol 'A'

    >>> x = Leaf(symbol='A')
    >>> print(repr(x))
    (LEAF {'symbol': 'A'})
    """
    repr_string = '(LEAF %s)'

    def __init__(self, **data):
        super().__init__()
        self.data = data
        self.parent = None

    def __repr__(self):
        """Representation of leaf

        Returns
        -------
        str
            string representation of leaf

        """
        return self.repr_string % str(self)

    def __str__(self):
        """String representation of leaf

        Returns
        -------
        str
            string representation of leaf data's
        """
        return str(self.data)

    def __iter__(self):
        yield self


class BaseTree(ABC, Leaf):
    """Base class for trees
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
    
    def __str__(self):
        """String representation of a tree

        Returns
        -------
        str
            string representation of a tree and all its children recursively
        """
        return ''.join(str(x) for x in self.children)

    def __iter__(self):
        """Iterator over the tree,
        deep first pre-order traversal of a tree

        Yields
        ------
        :obj:`Leaf`
            all nodes of a tree in deep first pre-order
        """
        
        yield self
        for child in list(self.children): # TODO remove list casting
            if child:
                yield from child

        pass
    
    pass

class KTree(BaseTree):
    """
    A simple k-ary tree

    """
    repr_string = '(KTREE %s)'

    def __init__(self):
        super().__init__(**dict())
        self.__children =  []

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
        child : :obj:`Btree`
            a btree instance

        Raises
        ------
        AssertionError
           if child is not orphaned and its parent is not set to None
        TypeError
           if child is not a Btree instance
        """
        if not isinstance(child, BTree):
            raise TypeError('child wrong type %s, try to push it in %s' % (child, self))

        if child.parent is not None:
            raise AssertionError('child %s is not orphaned, parent %s' % (child, child.parent))
        
        child.parent = self
        self.__children.append(children)


class BTreeRight(object):
    pass

class BTreeLeft(object):
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
        super().__init__(**dict())
        self.__children =  OrderedDict((x,None)for x in (BTree.LEFT, BTree.RIGHT))
        pass

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
            a child, must be a Leaf or a Ktree instance and a sub class of BtreeLeft or BtreeRight

        Raises
        ------
        AssertionError
           if child is not orphaned and its parent is not set to None
        TypeError
           if child is not a Leaf or a Ktree instance
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

def shallow_copy(tree):
    """Do a shallow copy of tree

    Examples
    --------
    >>> x = Leaf(symbol='A')
    >>> y = shallow_copy(x)
    >>> print(y)
    {'symbol': 'A'}

    Parameters
    ----------
    tree: :obj:`tree`
       a tree

    Returns
    -------
    :obj:`tree`
        orphaned shallow copy of a tree
    """
    t_copy = type(tree)(**tree.data)
    
    if isinstance(tree, BaseTree):
        for child in tree.children:
            t_copy.push(shallow_copy(child))
            
    return t_copy

