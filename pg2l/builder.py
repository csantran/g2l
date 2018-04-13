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

    # >>> p = builder(
    #         [G.LETTER, 'ABCDEF'],
    #         [G.NUMBER, range(5)],
    #         [G.LBR],
    #         [G.RBR],
    #         [G.parametric, dict(
    #             domain = G.successor,
    #             name = 'weight',                  # can be G.predecessor and/or G.successor
    #             initial_value = 0,                # derivation of G.axiom into G.succ_string
    #             variables = [G.node, G.jump],     # and G.pred_string
    #             α = lambda data: data.update(weight=data['weight']+1),
    #             β = lambda data: data.update(weight=data['weight']-1))
    #             ],

    #         [G.g2l, 
    #             dict(
    #                 cellular = G.node & G.OP_REWITE & G.node
    #             ),

    #             dict(
    #                 cellular_acropet =  G.node & G.OP_REWRITE & G.node
    #                 context = G.context & G.OP_LCONTEXT
    #                 ),

    #             dict(
    #                 cellular_basipet = G.node & G.OP_REWRITE & G.node
    #                 context = G.OP_RCONTEXT & G.context
    #                 ),

    #             dict(
    #                 death = G.node & G.OP_REWRITE & G.empty
    #                 context = (G.context & G.OP_CONTEXT)
    #                         | (G.empty & G.OP_CONTEXT)



    #             ),

            


    # )
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
