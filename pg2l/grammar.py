from abc import ABC, abstractmethod

class AbstractGrammar(ABC):

    @abstractmethod
    def __init__(self, *declarations):
        pass

    # @property
    # @abstractmethod
    # def terminals(self):
    #     raise NotImplementedError()

    # @property
    # @abstractmethod
    # def nonterminals(self):
    #     raise NotImplementedError()

    # @property
    # @abstractmethod
    # def axiom(self):
    #     raise NotImplementedError()

    # @property
    # @abstractmethod
    # def productions(self):
    #     raise NotImplementedError()

    # @abstractmethod
    # def generate(self, max_recursion=-1):
    #     raise NotImplementedError()

    # @abstractmethod
    # def __repr__(self):
    #     raise NotImplementedError()

def grammar(axiom, *productions):
    """factory"""
    if isinstance(axiom, type):
        return ...
    elif isinstance(axiom, object):
        return ...

