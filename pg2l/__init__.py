# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>

# registering terminals and nonterminals with decorator in grammar (see grammar.py),
# but without polluting the namespace
from .parser import terminal as __
from .parser import nonterminal as __
