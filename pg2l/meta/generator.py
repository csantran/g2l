from random import choice

class SimpleGenerator(object):

    @staticmethod
    def generate(G, sentential_form, nb_iteration=-1, probability=None):

        tape = sentential_form
        new_tape = []
        count = 0

        while True:
            print('generation', count, tape)

            for i, symbol in enumerate(list(tape)):

                # empty rule
                if symbol == 'empty':
                    pass

                # terminal, identity production, nothing to change
                elif symbol in G.terminals:
                    new_tape.append(symbol)

                # nonterminal
                else:
                    new_tape += choice([rhs for lhs, rhs in G.productions if lhs == symbol])
                    
            count += 1
            if tape != new_tape and not (nb_iteration != -1 and count == nb_iteration):
                tape = new_tape
                new_tape = []
                continue

            break


        for x in new_tape:
            if x in G.terminals:
                print('X', x)
        
        return ''.join(str(x) for x in new_tape)
