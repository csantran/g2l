# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
def decorator_register_factory(register):
    def _register_with_grammar(item):
        def _register_this(cls):
            register[item] = cls
            return cls

        return _register_this

    return _register_with_grammar
