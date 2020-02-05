### IMPORTS ###

from LearningRules import *
from Game import *
import Database.MultiGame as MDB
import MyMath as MyMath


### SET PARAMETERS ###

# choose learning rule from "CF", "EWA", "FP", "FWC", "NE", "RL"
learning_rule = "FWC"

# choose experiment ID from 1 to 6 (see MultiGameDB in Database.MultiGame)
experiment_ID = 1

# choose the number of repetitions of the simulation
num_trials = 1000


### INITIALISE THE SIMULATION EXPERIMENT ###

# read data from the database MultiGameDB
sequence = MDB.MultiGameDB[experiment_ID-1][1]
num_agents = MDB.MultiGameDB[experiment_ID-1][2]
source = MDB.MultiGameDB[experiment_ID-1][3]
result_data = MDB.MultiGameDB[experiment_ID-1][4]
result_data_description = MDB.MultiGameDB[experiment_ID-1][5]


# initialize the sequence as an array of objects of the class Game
game_sequence = []
for game_payoffs in sequence:
    if game_payoffs[0][0] > game_payoffs[1][0]:
        game_type = 'SH'
    else:
        game_type = 'PD'
    game_sequence.append(Game(game_type, game_payoffs))

# initialize the set of agents as objects of the class of the appropriate learning rule
agents = []
for index in range(num_agents):

    if learning_rule == "CF":
        new_agent = CF()
    elif learning_rule == "EWA":
        new_agent = EWA()
    elif learning_rule == "FP":
        new_agent = FP()
    elif learning_rule == "FWC":
        new_agent = FWC()
    elif learning_rule == "RL":
        new_agent = RL()
    else:
        new_agent = NE()

    agents.append(new_agent)


### RUN THE SIMULATION EXPERIMENT ###

# initiate the array that records rounds-by-round cooperation rates averaged over all agents and trials
sim_coop_rates = []
for index in range(len(game_sequence)):
    sim_coop_rates.append(0.0)

# run the trials
for trial in range(num_trials):

    # reset agents
    for agent in agents:
        agent.reset()

    # conduct the current rounds for the current trial
    for current_round in range(len(game_sequence)):

        # reset the counter for the number of cooperation per round
        num_coop = 0

        # take the cuurent game from the sequence
        current_game = game_sequence[current_round]

        # create a set of randomly matched pairs of agents
        agent_pairs = MyMath.random_pairs(agents)

        # for experiment 1: reset half of the agents after 12 rounds
        if experiment_ID == 1 and current_round == 12:
            for index in range(num_agents/2):
                agents[index].reset()


        # each pair of agents interacts
        for pair in agent_pairs:

            agent1 = pair[0]
            agent2 = pair[1]

            # make the choices according to the learning mechanism's choice rule
            choice1 = agent1.choice(current_game)
            choice2 = agent2.choice(current_game)

            # always update agents, except for experiments 5-8 (Ahn et al. 2001), final 4 games
            if experiment_ID < 3 or current_round < 8:
                # make the updates according to the learning mechanism's update rule
                agent1.update(current_game, choice1, choice2)
                agent2.update(current_game, choice2, choice1)

            # update the counter for the number cooperation per round
            if choice1 == 'C':
                num_coop += 1
            if choice2 == 'C':
                num_coop += 1

        # update the array that records rounds-by-round cooperation rates averaged over all agents and trials
        sim_coop_rates[current_round] += num_coop*1.0/(num_agents*num_trials)



### PRINT THE SIMULATION RESULTS ###


print result_data_description+": laboratory VS simulation (sequence by "+source+", learning rule: "+learning_rule+")"
print

# print round-by-round results for the experiments by Schmidt et al. (2001)
if experiment_ID == 1:

    print "RbR coop rates laboratory: \t",

    for rate in result_data:
        print round(rate, 3), "\t",
    print

    print "RbR coop rates sim. of "+learning_rule+":\t",
    for rate in sim_coop_rates:
        print round(rate,3), "\t",
    print

# print round-by-round results for the experiments by Rankin et al. (2000)
elif experiment_ID == 2:

    print "avg coop rates (first 10 rounds) laboratory : \t", result_data[0], "\t", result_data[1]
    print "avg coop rates (first 10 rounds) sim. of "+learning_rule+":\t", round(sum(sim_coop_rates[0:10])/len(sim_coop_rates[0:10]),3),
    print "\t["+str(round((sim_coop_rates[1]+sim_coop_rates[3]+sim_coop_rates[5]+sim_coop_rates[7]+sim_coop_rates[9])/5,3))+",",
    print str(round((sim_coop_rates[0]+sim_coop_rates[2]+sim_coop_rates[4]+sim_coop_rates[6]+sim_coop_rates[8])/5,3))+"]"
    print
    print "avg coop rates (last 10 rounds) laboratory : \t", result_data[2], "\t", result_data[3]
    print "avg coop rates (last 10 rounds) sim. of " + learning_rule + ":\t", round(sum(sim_coop_rates[65:]) / len(sim_coop_rates[65:]),3),
    print "\t["+str(round((sim_coop_rates[66]+sim_coop_rates[69]+sim_coop_rates[70]+sim_coop_rates[71]+sim_coop_rates[74])/5,3))+",",
    print str(round((sim_coop_rates[65]+sim_coop_rates[67]+sim_coop_rates[68]+sim_coop_rates[72]+sim_coop_rates[73])/5,3))+"]"


#print average cooperation rates over four PD games for the experiments by Ahn et al. (2001)
else:

    print "RbR coop rates laboratory: \t",
    for rate in result_data:
        print round(rate, 3), "\t",
    print

    print "RbR coop rates sim. of "+learning_rule+":\t",
    for rate in sim_coop_rates:
        if sim_coop_rates.index(rate) > 7:
            print round(rate,3), "\t",
    print
