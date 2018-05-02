from abc import ABC, abstractmethod


class AbstractGrammar(ABC):

    @staticmethod
    @abstractmethod
    def from_string(self, *args, **kwargs):
        raise NotImplementedError()


    @staticmethod
    @abstractmethod
    def from_declaration(self, *args, **kwargs):
        raise NotImplementedError()
