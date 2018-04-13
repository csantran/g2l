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

class MetaDeclaration(object):
    """a singleton filled by MetaSymbol, contain all grammar symbols, created dynamicaly"""
    terminals = []
    nonterminals = []
    variables = []
    constants = []
    pass

class MetaSymbol(AbstractMetaSymbol):
    """Symbol metaclass,
    All concrete symbol must use this metaclass
    Implement the class attribut name"""

    def __new__(mcs, name, bases, classdict):
        # look for __meta_name
        ismetasymbol = False
        
        for base in bases:
            if hasattr(base, '_meta_symbol'):
                print('BASES', name, [x.__name__ for x in bases])
                classdict['symbol'] = base._meta_symbol(name)
                
                ismetasymbol = True
                break
            
        cls = type(name, bases, classdict)
        if ismetasymbol:
            setattr(MetaDeclaration, classdict['symbol'], cls)

            if classdict['symbol'].islower():
                MetaDeclaration.nonterminals.append(cls)
            elif classdict['symbol'].isupper():
                MetaDeclaration.terminals.append(cls)
                if bases[0].__name__ == 'Constant':       # Create anothers metaclasses for do this
                    MetaDeclaration.constants.append(cls)
                elif bases[0].__name__ == 'Variable':
                    MetaDeclaration.variables.append(cls)
                else:
                    raise Exception(1)
            else:
                raise Exception(2)

        return cls

class AbstractSymbol(metaclass=AbstractMetaSymbol):
    """Abstract Base Class for grammar terminal and nonterminal symbol"""

    @property
    @abstractmethod
    def symbol(self):
        """the symbol name's, a string

        Returns
        -------
        str:
           name
        """
        # this property becomes a class attribut when it is implemented by MetaSymbol
        # so we can get the name attribut of the concrete symbol class without having
        # to instantiate it
        raise NotImplementedError()

    @abstractmethod
    def _meta_symbol(self, name):
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
        return '(%s %s)' % (str(self.symbol), str(self))

class AbstractSymbolString(AbstractSymbol):
    """
    nonterminal leaf object, a string

    Parameters
    ----------
    string : str
        a string
    """
    _string = None
    
    def __init__(self, string):
        super().__init__()
        self._string = str(string)

    def __str__(self):
        return self._string

class AbstractTerminalSymbol(AbstractSymbolString):
    """Abstract base class for grammar terminal symbols"""
    _meta_symbol = lambda name : name.upper()
    
class AbstractNonTerminalLeafSymbol(AbstractSymbolString):
    """Abstract base class for grammar nonterminal leaf symbols"""
    _meta_symbol = lambda name : name.lower()

class AbstractNonTerminalBranchSymbol(AbstractSymbol):
    """Abstract base class for grammar nonterminal branch symbols"""
    _meta_symbol = lambda name : name.lower()
