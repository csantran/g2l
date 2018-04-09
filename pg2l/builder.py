# -*- coding : utf-8 -*-
#    Copyright (C) 2018 by
#    Cédric Santran <santrancedric@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#    Cédric Santran <santrancedric@gmail.com>

def builder(*args):
    """Build the parser from args

    Examples
    --------
    the goal is to get this

    # >>> p = builder(                              # simplified grammar :
    #         (G.LETTER, 'ABCDEF'),                 # LETTER := 'A'|'B'|'C'|'D'|'E'|'F'
    #         (G.NUMBER, range(5)),                 # NUMBER := 0|1|2|3|4
    #         (G.LBR, '['),                         # LBR := '['
    #         (G.RBR, ']'),                         # RBR := ']'
    #         (G.OP_REWRITE, ':'),                  # OP_REWRITE := ':'

    #         (G.parametric, dict(                  # PARAMETRIC := 'α'|'β'
    #             α = lambda x: x,
    #             β = lambda x: x)
    #             ),

    #         (G.successor, derive_string(            # successor := axiom
    #                                                            | p_node
    #             G.p_node:(                        #            | successor p_node
    #                 G.parametric,                 # p_node := PARAMETRIC node
    #                 G.node)}
    #             ),

    #         )
    #         (G.successor, derive_axiom(             # successor := axiom
    #             (G.p_node, (                        #            | p_node
    #                 G.parametric,                   #            | successor p_node
    #                 G.node)),                       # p_node := PARAMETRIC node
    #             (G.number, (
    #                 G.parametric,
    #                 G.number)),
    #             ),
    #         )
    #         (G.g0l, dict(                         # g0l := node OP_REWRITE axiom
    #             predecessor = (G.node, G.module), #      | module OP_REWRITE axiom
    #             successor = (G.successor)
    #          )),
    #         (G.g0l, dict(                         #      | jump OP_REWRITE jump
    #             predecessor = (G.jump),           #      | jump OP_REWRITE axiom
    #             successor = (G.jump, G.successor)
    #          ))                                   # node, module,... are loaded automatically
    #         )
    """
    raise NotImplementedError()
