import random

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
