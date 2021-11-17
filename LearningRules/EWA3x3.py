import MyMath as MyMath
import random

class EWA3x3:

    ### CONSTRUCTOR ###

    def __init__(self):

        # current probability for cooperation
        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3

        # history sequence of opponents' behavior
        self.history_opponents_move = [0,0,0]

        # attraction values for cooperation and defection (initialized with first choice)
        self.attractionA = -1
        self.attractionB = -1
        self.attractionC = -1

        # experience weight (initially set to 1.0)
        self.experience = 1.0

        # change detector value (initialized with first update)
        self.predictability = -1

        # regret factors for cooperation and defection (initialized with first update)
        self.regretA = -1
        self.regretB = -1
        self.regretC = -1


    ### CHOICE FUNCTION ###

    def choice(self, game):

        # initialize attractions value due to the first game:
        if self.attractionA == -1 or self.attractionB == -1 or self.attractionC == -1:
            #initial_attraction_values = MyMath.cognitive_hierarchy(game.payoffs, 1.5)
            self.attractionA = 0.0
            self.attractionB = 0.0
            self.attractionC = 0.0

            self.probA = 1.0 / 3
            self.probB = 1.0 / 3
            self.probC = 1.0 / 3

        else:
            # compute cooperation probability due to attraction values
            self.probA = self.attractionA / (self.attractionA + self.attractionB + self.attractionC)
            self.probB = self.attractionB / (self.attractionA + self.attractionB + self.attractionC)
            self.probC = self.attractionC / (self.attractionA + self.attractionB + self.attractionC)

        # make a probabilistic choice
        random_draw = random.random()

        if random_draw < self.probA:
            choice = 'A'
        elif random_draw < (self.probA + self.probB):
            choice = 'B'
        else:
            choice = 'C'

        return choice

    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):


        # fill history of opponents' behavior with 0 for cooperation and 1 for defection
        if opponent_choice == 'A':
            self.history_opponents_move[0] += 1
            opponentA = 1.0
            opponentB = 0.0
            opponentC = 0.0
        elif opponent_choice == 'B':
            self.history_opponents_move[1] += 1
            opponentA = 0.0
            opponentB = 1.0
            opponentC = 0.0
        else:
            self.history_opponents_move[2] += 1
            opponentA = 0.0
            opponentB = 0.0
            opponentC = 1.0

        # compute frequencies of opponents cooperation and defection according to history
        frequency_opponentsA = self.history_opponents_move[0] / sum(self.history_opponents_move)
        frequency_opponentsB = self.history_opponents_move[1] / sum(self.history_opponents_move)
        frequency_opponentsC = self.history_opponents_move[2] / sum(self.history_opponents_move)

        # compute surprise values for cooperation and defection in the last round
        surpriseA = (frequency_opponentsA - opponentA) ** 2
        surpriseB = (frequency_opponentsB - opponentB) ** 2
        surpriseC = (frequency_opponentsC - opponentC) ** 2

        # compute predictability as how unsurprising the opponent's choice has been
        self.predictability = 1.0 - (0.5 * (surpriseA + surpriseB + surpriseC))

        # compute current payoffs and payoffs if cooperated or defected
        if my_choice == 'A':
            my_index = 0
        elif my_choice == 'B':
            my_index = 1
        else:
            my_index = 2

        if opponent_choice == 'A':
            op_index = 0
        elif opponent_choice == 'B':
            op_index = 1
        else:
            op_index = 2

        current_payoff = game.payoffs[my_index][op_index]
        payoffA = game.payoffs[0][op_index]
        payoffB = game.payoffs[1][op_index]
        payoffC = game.payoffs[2][op_index]

        # compute regret values
        if current_payoff < payoffA:
            self.regretA = 0.5
        else:
            self.regretA = 0.0

        if current_payoff < payoffB:
            self.regretB = 0.5
        else:
            self.regretB = 0.0

        if current_payoff < payoffC:
            self.regretC = 0.5
        else:
            self.regretC = 0.0

        # compute updated experience value
        new_experience = self.experience * self.predictability + 1.0

        # compute regret factors for cooperation and defection
        regret_factorA = payoffA * (self.regretA + (1.0 - self.regretA) * MyMath.ident(my_choice, 'A'))
        regret_factorB = payoffB * (self.regretB + (1.0 - self.regretB) * MyMath.ident(my_choice, 'B'))
        regret_factorC = payoffC * (self.regretC + (1.0 - self.regretC) * MyMath.ident(my_choice, 'C'))

        # update attraction values
        self.attractionA = (self.predictability*self.experience*self.attractionA+regret_factorA)/new_experience
        self.attractionB = (self.predictability*self.experience*self.attractionB+regret_factorB)/new_experience
        self.attractionC = (self.predictability*self.experience*self.attractionC+regret_factorC)/new_experience

        # update experience value
        self.experience = new_experience


    ### RESET FUNCTION ###

    def reset(self):

        # current probability for cooperation
        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3

        # history sequence of opponents' behavior
        self.history_opponents_move = [0, 0, 0]

        # attraction values for cooperation and defection (initialized with first choice)
        self.attractionA = -1
        self.attractionB = -1
        self.attractionC = -1

        # experience weight (initially set to 1.0)
        self.experience = 1.0

        # change detector value (initialized with first update)
        self.predictability = -1

        # regret factors for cooperation and defection (initialized with first update)
        self.regretA = -1
        self.regretB = -1
        self.regretC = -1