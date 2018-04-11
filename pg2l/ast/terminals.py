# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from .base import AbstractTerminalSymbol, MetaSymbol

class Char(AbstractTerminalSymbol):
    pass

class Letter(Char, metaclass=MetaSymbol):
    pass

class Number(Char, metaclass=MetaSymbol):
    pass

class Lbr(Char, metaclass=MetaSymbol):
    pass

class Rbr(Char, metaclass=MetaSymbol):
    pass

class Op_Rewrite(Char, metaclass=MetaSymbol):
    pass

class Op_GLContext(Char, metaclass=MetaSymbol):
    pass

class Op_GRContext(Char, metaclass=MetaSymbol):
    pass

class Op_SLContext(Char, metaclass=MetaSymbol):
    pass

class Op_SRContext(Char, metaclass=MetaSymbol):
    pass
