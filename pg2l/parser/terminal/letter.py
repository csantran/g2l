from pg2l import ast
from pg2l import grammar

@grammar.register('LETTER')
class LetterLexer(grammar.Terminal):
    def __init__(self, letters):
        assert isinstance(letters, str)
        
        self.tokens += ["LETTER"]
        self.variables += list(letters)
        
        self.t_LETTER = r'[%s]' % letters
