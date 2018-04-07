from pg2l import grammar
from .base import BaseLexer

DEFAULT_LBR = '['
DEFAULT_RBR = ']'


class Constant(BaseLexer, grammar.Terminal):
    def __init__(self, constant, grammar_constant):
        self.tokens += [grammar_constant]
        self.constants += [constant]
        setattr(self, 't_%s' % grammar_constant, r'\%s' % constant)

    
@grammar.register('LBR')
class LBRLexer(Constant):
    def __init__(self, constant=DEFAULT_LBR):
        Constant.__init__(self, constant, grammar.Grammar.LBR)

@grammar.register('RBR')
class RBRLexer(Constant):
    def __init__(self, constant=DEFAULT_RBR):
        Constant.__init__(self, constant, grammar.Grammar.RBR)
