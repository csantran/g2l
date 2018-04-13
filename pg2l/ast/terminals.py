# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import AbstractTerminalSymbol, MetaSymbol

class Variable(AbstractTerminalSymbol):
    pass

class Constant(AbstractTerminalSymbol):
    pass

class Letter(Variable, metaclass=MetaSymbol):
    pass

class Number(Variable, metaclass=MetaSymbol):
    pass

class Lbr(Constant, metaclass=MetaSymbol):
    pass

class Rbr(Constant, metaclass=MetaSymbol):
    pass

class Rewrite(Constant, metaclass=MetaSymbol):
    pass

class GLContext(Constant, metaclass=MetaSymbol):
    pass

class GRContext(Constant, metaclass=MetaSymbol):
    pass

class SLContext(Constant, metaclass=MetaSymbol):
    pass

class SRContext(Constant, metaclass=MetaSymbol):
    pass
