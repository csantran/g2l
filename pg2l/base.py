from abc import ABC, abstractmethod


class AbstractGrammar(ABC):

    @staticmethod
    @abstractmethod
    def from_string():
        raise NotImplementedError()


    @staticmethod
    @abstractmethod
    def from_declaration():
        raise NotImplementedError()
            
