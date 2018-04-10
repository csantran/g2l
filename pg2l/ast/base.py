# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from abc import ABC, abstractmethod


class AbstractGrammarSymbol(ABC):
    _repr_string = '(%s %s)'

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        return self._repr_string % (str(self.name), str(self))

class AbstractTerminal(AbstractGrammarSymbol):
    _value = None

    @property
    def value(self):
        return self._value

    @property
    def name(self):
        return type(self).__name__.upper()

    def __str__(self):
        return self.value
    
class AbstractNonTerminal(AbstractGrammarSymbol):

    @property
    def name(self):
        return type(self).__name__.lower()
