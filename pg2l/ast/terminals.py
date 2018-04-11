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

