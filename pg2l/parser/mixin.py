# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>
from abc import ABC


class AbstractMixin(ABC):
    """Mixin abstract base class"""

def mixin(name, *params):
    """Create a mixing class with many base classes and call each __init__ base class with specific
    args and kargs.
    The name string is the class name and becomes the __name__ attribute of the mixin class.
    Each item of the iterable params must itself be an iterable with exactly three objects.
    The first object is the base class to mix, base class must be a subclass of AbstractMixin.
    As for the second and the third, respectively an iterable and a mapping, they will be unpacked
    during the call of __init__ method of the first object.

    This function is like to type built-in function. The Goal is to provide a mechanism to contruct
    a mixin class when the __init__ methods of the base classes do not have the same footprint.
    This allows to create a new class instance where each bass class is initialized with its own
    parameters.

    Parameters
    ----------
    name : obj:`str`
       name of the mixin class, becomes the __name__ attribute
    params : obj:`*iterable`
       iterable of iterable of form [base, iterable, mapping] where base is the base class,
       iterable and mapping object act as args and kwargs when calling base class __init__

    Returns
    -------
    obj:`cls`
       the new mixin class
    """
    # unpacking bases
    class MixinTemplate(*list(zip(*params))[0]):
        """Template for mixins"""

        def __init__(self):
            # call __init__ for all bases in params with related args and kwargs
            for cls, args, kwargs in params:
                cls.__init__(self, *args, **kwargs)

    # renaming template
    MixinTemplate.__qualname__ = name

    return MixinTemplate()
