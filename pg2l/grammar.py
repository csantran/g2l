import inspect

class Terminal(object):
    pass

class NonTerminal(object):
    pass

class Grammar(object):
    pass

lexers = {}
parsers = {}

def register(element):
    def __register_element_with(this_cls):
        bases = inspect.getmro(this_cls)
        
        assert not hasattr(Grammar, element)
        setattr(Grammar, element, element)
        
        if Terminal in bases:
            lexers[element] = this_cls
        elif NonTerminal in bases:
            parsers[element] = this_cls
        else:
            raise TypeError(this_cls)

        return this_cls

    return __register_element_with
