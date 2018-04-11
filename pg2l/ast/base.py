# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from abc import ABCMeta, abstractmethod

class AbstractMetaSymbol(ABCMeta):
    """Abstract symbol metaclass"""


class MetaSymbol(AbstractMetaSymbol):
    """Symbol metaclass,
    All concrete symbol must use this metaclass
    Implement the class attribut name"""

    def __new__(mcs, name, bases, classdict):
        # look for __meta_name
        for base in bases:
            if hasattr(base, '_meta_name'):
                classdict['name'] = base._meta_name(name)
                break

        return type(name, bases, classdict)

class AbstractSymbol(metaclass=AbstractMetaSymbol):
    """Abstract Base Class for grammar terminal and nonterminal symbol"""
    @property
    @abstractmethod
    def name(self):
        # this property becomes a class attribut when it is implemented by MetaSymbol
        # so we can get the name attribut of the concrete symbol class without having
        # to instantiate it
        raise NotImplementedError()

    @abstractmethod
    def _meta_name(self, name):
        """hook for formatting class name

        Parameters
        ----------
        name : :obj:`str`
             the original class name

        Returns
        -------
        :obj:`str`
             the new class name"""
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        return '(%s %s)' % (str(self.name), str(self))

class AbstractTerminalSymbol(AbstractSymbol):
    """Abstract base class for grammar terminal symbols"""
    _meta_name = lambda name : name.upper()

    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError()

    def __str__(self):
        return str(self.value)

class AbstractNonTerminalSymbol(AbstractSymbol):
    """Abstract base class for grammar nonterminal symbols"""
    _meta_name = lambda name : name.lower()
