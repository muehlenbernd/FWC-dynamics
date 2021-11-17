import random
from LearningRules.EWA3x3 import *
from LearningRules.FP3x3 import *
from LearningRules.FWC3x3 import *
from LearningRules.RL3x3 import *
from LearningRules.NE3x3 import *
from LearningRules.CF3x3 import *

### makes a probabilistic choice with respect to the input probability ###
def prob_choice(prob):

    is_chosen = False

    value = random.random()
    if value < prob:
        is_chosen= True

    return is_chosen


### returns randomly chosen pairs from an input array ###
def random_pairs(input_array):

    # make a copy of the input array to work with
    input_array_copy = []
    for entry in input_array:
        input_array_copy.append(entry)

    # create an array of pairs
    pair_array = []
    for pair_count in range(len(input_array)/2):
        index1 = random.randint(0,len(input_array_copy)-1)
        pair_member1 = input_array_copy.pop(index1)
        index2 = random.randint(0,len(input_array_copy)-1)
        pair_member2 = input_array_copy.pop(index2)
        pair_array.append([pair_member1,pair_member2])

    # return array of pairs
    return pair_array



### normalizes a triple of values, so that each value in non-negative and their sum is 1 ###
def normalize_triple(triple):

    # make all values >= 0.0
    if triple[0] < 0.0:
        triple[0] = 0.0

    if triple[1] < 0.0:
        triple[1] = 0.0

    if triple[2] < 0.0:
        triple[2] = 0.0

    # normalize so that triple sum is 1.0
    triple_sum = sum(triple)

    triple[0] /= triple_sum
    triple[1] /= triple_sum
    triple[2] /= triple_sum

    return triple


### normalizes a triple of values, so that each value in non-negative and their sum is 1 ###
def normalize_quartuple(quartuple):

    # make all values >= 0.0
    if quartuple[0] < 0.0:
        quartuple[0] = 0.0

    if quartuple[1] < 0.0:
        quartuple[1] = 0.0

    if quartuple[2] < 0.0:
        quartuple[2] = 0.0

    if quartuple[3] < 0.0:
        quartuple[3] = 0.0

    # normalize so that triple sum is 1.0
    quartuple_sum = sum(quartuple)

    quartuple[0] /= quartuple_sum
    quartuple[1] /= quartuple_sum
    quartuple[2] /= quartuple_sum
    quartuple[3] /= quartuple_sum

    return quartuple


### returns probabilities for one move or the other with respect to a cognitive hierarchy level and ###
### a game with two choices. For more details see Camerer, Ho and Chong (2004)

def cognitive_hierarchy(game, level=0):

    a = game[0][0]
    b = game[0][1]
    c = game[1][0]
    d = game[1][1]

    # level 0:
    p0 = [0.5,0.5]
    EU0 = [p0[0]*a + p0[1]*b , p0[0]*c + p0[1]*d]

    # level 1:
    p1 = [EU0[0]/sum(EU0), EU0[1]/sum(EU0)]
    EU1 = [p1[0]*a + p1[1]*b , p1[0]*c + p1[1]*d]

    # level 2:
    p2 = [EU1[0] / sum(EU1), EU1[1] / sum(EU1)]

    # level 0.5
    p05 = [(p0[0]+p1[0])/2.0, (p0[1]+p1[1])/2.0]

    # level 1.5
    p15 = [(p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0]

    result_register = p0

    if level == 0.5:
        result_register = p05
    elif level == 1 or level == 1.0:
        result_register = p1
    elif level == 1.5:
        result_register = p15
    elif level == 2 or level == 2.0:
        result_register = p2

    return result_register


### resturns 1 if s1 and s2 are identical, else 0 ###
def ident(s1, s2):

    if s1 == s2:
        return 1
    else:
        return 0


# computes the mean square error of two sequences with the same length
def mean_square_error(sequence1, sequence2):

    mse = 0.0

    for index in range(len(sequence1)):

        mse += (((sequence1[index]-sequence2[index])**2)/len(sequence1))

    return mse


def simulate_avg3x3(current_game, num_agents, learning_rule, num_rounds, num_trials):

    # initialize the set of agents with the appropriate learning rule
    agents = []
    for index in range(num_agents):

        if learning_rule == "CF":
            new_agent = CF3x3()
        elif learning_rule == "EWA":
            new_agent = EWA3x3()
        elif learning_rule == "FP":
            new_agent = FP3x3()
        elif learning_rule == "FWC":
            new_agent = FWC3x3()
        elif learning_rule == "RL":
            new_agent = RL3x3()
        else:
            new_agent = NE3x3()

        agents.append(new_agent)

    ### RUN THE SIMULATION EXPERIMENT ###



    sim_coop_rates = []
    for index in range(num_rounds):
        sim_coop_rates.append([0.0,0.0,0.0])

    for trial in range(num_trials):

        # reset agents
        for agent in agents:
            agent.reset()

        #

        # trial_coop_rate = [0.0,0.0,0.0]

        for current_round in range(num_rounds):

            num_coop = [0,0,0]
            agent_pairs = MyMath.random_pairs(agents)

            for pair in agent_pairs:
                agent1 = pair[0]
                agent2 = pair[1]

                choice1 = agent1.choice(current_game)
                choice2 = agent2.choice(current_game)

                agent1.update(current_game, choice1, choice2)
                agent2.update(current_game, choice2, choice1)

                if choice1 == 'A':
                    num_coop[0] += 1
                    #trial_coop_rate[0] += (1.0 / (num_agents * num_rounds))
                elif choice1 == 'B':
                    num_coop[1] += 1
                    #trial_coop_rate[1] += (1.0 / (num_agents * num_rounds))
                elif choice1 == 'C':
                    num_coop[2] += 1
                    #trial_coop_rate[2] += (1.0 / (num_agents * num_rounds))

                if choice2 == 'A':
                    num_coop[0] += 1
                    #trial_coop_rate[0] += (1.0 / (num_agents * num_rounds))
                elif choice2 == 'B':
                    num_coop[1] += 1
                    #trial_coop_rate[1] += (1.0 / (num_agents * num_rounds))
                elif choice2 == 'C':
                    num_coop[2] += 1
                    #trial_coop_rate[2] += (1.0 / (num_agents * num_rounds))

            sim_coop_rates[current_round][0] += num_coop[0] * 1.0 / (num_agents * num_trials)
            sim_coop_rates[current_round][1] += num_coop[1] * 1.0 / (num_agents * num_trials)
            sim_coop_rates[current_round][2] += num_coop[2] * 1.0 / (num_agents * num_trials)

            # print trial_coop_rate

    #print "xxx", sim_coop_rates

    return sim_coop_rates