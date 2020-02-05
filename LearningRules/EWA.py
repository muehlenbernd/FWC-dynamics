import MyMath as MyMath

class EWA:

    ### CONSTRUCTOR ###

    def __init__(self):

        # current probability for cooperation
        self.prob_coop = 0.5

        # history sequence of opponents' behavior
        self.history_opponents_move = []

        # attraction values for cooperation and defection (initialized with first choice)
        self.attraction_coop = -1
        self.attraction_def = -1

        # experience weight (initially set to 1.0)
        self.experience = 1.0

        # change detector value (initialized with first update)
        self.predictability = -1

        # regret factors for cooperation and defection (initialized with first update)
        self.regret_coop = -1
        self.regret_def = -1


    ### CHOICE FUNCTION ###

    def choice(self, game):

        # initialize attractions value due to the first game:
        if self.attraction_coop == -1 or self.attraction_def == -1:
            initial_attraction_values = MyMath.cognitive_hierarchy(game.payoffs, 1.5)
            self.attraction_coop = initial_attraction_values[0]
            self.attraction_def = initial_attraction_values[1]

        # compute cooperation probability due to attraction values
        self.prob_coop = self.attraction_coop / (self.attraction_coop + self.attraction_def)

        # make a probabilistic choice
        if MyMath.prob_choice(self.prob_coop):
            choice = 'C'
        else:
            choice = 'D'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):


        # fill history of opponents' behavior with 0 for cooperation and 1 for defection
        if opponent_choice == 'C':
            self.history_opponents_move.append(0)
            opponent_coop = 1.0
        else:
            self.history_opponents_move.append(1)
            opponent_coop = 0.0

        # compute frequencies of opponents cooperation and defection according to history
        frequency_opponents_def = sum(self.history_opponents_move)*1.0/len(self.history_opponents_move)
        frequency_opponents_coop = 1.0 - frequency_opponents_def

        # compute surprise values for cooperation and defection in the last round
        surprise_coop = (frequency_opponents_coop - opponent_coop) ** 2
        surprise_def = (frequency_opponents_def - (1.0 - opponent_coop)) ** 2

        # compute predictability as how unsurprising the opponent's choice has been
        self.predictability = 1.0 - (0.5 * (surprise_coop + surprise_def))

        # compute current payoffs and payoffs if cooperated or defected
        current_payoff = game.payoffs[0 if my_choice == 'C' else 1][0 if opponent_choice == 'C' else 1]
        payoff_coop = game.payoffs[0][0 if opponent_choice == 'C' else 1]
        payoff_def = game.payoffs[1][0 if opponent_choice == 'C' else 1]

        # compute regret values
        if current_payoff < payoff_coop:
            self.regret_coop = 0.5
        else:
            self.regret_coop = 0.0

        if current_payoff < payoff_def:
            self.regret_def = 0.5
        else:
            self.regret_def = 0.0

        # compute updated experience value
        new_experience = self.experience * self.predictability + 1.0

        # compute regret factors for cooperation and defection
        regret_factor_coop = payoff_coop * (self.regret_coop + (1.0 - self.regret_coop) * MyMath.ident(my_choice,'C'))
        regret_factor_def = payoff_def * (self.regret_def + (1.0 - self.regret_def) * MyMath.ident(my_choice, 'D'))

        # update attraction values
        self.attraction_coop = (self.predictability*self.experience*self.attraction_coop+regret_factor_coop)/new_experience
        self.attraction_def = (self.predictability*self.experience*self.attraction_def+regret_factor_def)/new_experience

        # update experience value
        self.experience = new_experience


    ### RESET FUNCTION ###

    def reset(self):

        # current probability for cooperation
        self.prob_coop = 0.5

        # history sequence of opponents' behavior
        self.history_opponents_move = []

        # attraction values for cooperation and defection (initialized with first choice)
        self.attraction_coop = -1
        self.attraction_def = -1

        # experience weight (initially set to 1.0)
        self.experience = 1.0

        # change detector value (initialized with first update)
        self.predictability = -1

        # regret factors for cooperation and defection (initialized with first update)
        self.regret_coop = -1
        self.regret_def = -1
