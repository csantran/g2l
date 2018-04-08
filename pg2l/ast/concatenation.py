# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>

def concatenation(v, w):
    """concatenation of two word u and v
    .. math:: 
       concatenation (v , w) = v \\cdot w \\rightarrow vw

    Examples
    --------
    Simple concatination example:

    # >>> s = SYMBOL('A')
    # >>> j = JUMP(1)
    # >>> a = concatenation(s, j)
    # >>> repr(A)
    # (CSYM A1)
    # >>> k = JUMP(2)
    # >>> a = concatenation(A, k)
    # >>> repr(A)
    # (CSYM A12)
    # >>> b = SYMBOL('B')
    # >>> c = SYMBOL('C')
    # >>> axiom = reduce(concatenation, (A, B, C))
    # >>> repr(axiom)
    # (AXIOM A12BC)

    Parameters
    ----------
    v : :obj:`Leaf`
        a word, any :obj:`Leaf` or :obj:`BaseTree` object
    w : :obj:`Leaf`
        a word, any :obj:`Leaf` or :obj:`BaseTree` object

    Returns
    -------
    vw : :obj:`BaseTree`
        the new word vw
    """
    raise NotImplementedError()
