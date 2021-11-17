### IMPORTS ###

from LearningRules import *
from Game import *
import Database.SingleGame as SDB
import MyMath as MyMath


### SET PARAMETERS ###

# choose learning rule from "CF", "EWA", "FP", "FWC", "NE", "RL"
learning_rule = "FWC"

# choose game by ID from 1 to 45
game_ID = 1

# choose the number of repetitions of the simulation
num_trials = 1000


### INITIALISE THE SIMULATION EXPERIMENT ###

# read data from the database SingleGameDB
game_payoffs = SDB.SingleGameDB[game_ID-1][1]
game_type = SDB.SingleGameDB[game_ID-1][2]
coop_avg = SDB.SingleGameDB[game_ID-1][3]
num_rounds = SDB.SingleGameDB[game_ID-1][4]
num_agents = SDB.SingleGameDB[game_ID-1][6]
coop_rates = SDB.SingleGameDB[game_ID-1][8]

# initialize the game under investigation as an object of the class Game
current_game = Game(game_type, game_payoffs)

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
for index in range(num_rounds):
    sim_coop_rates.append(0.0)

# run the trials
for trial in range(num_trials):

    # reset agents
    for agent in agents:
        agent.reset()

    # conduct the current rounds for the current trial
    for current_round in range(num_rounds):

        # reset the counter for the number of cooperation per round
        num_coop = 0

        # create a set of randomly matched pairs of agents
        agent_pairs = MyMath.random_pairs(agents)

        # each pair of agents interacts
        for pair in agent_pairs:

            agent1 = pair[0]
            agent2 = pair[1]

            # make the choices according to the learning mechanism's choice rule
            choice1 = agent1.choice(current_game)
            choice2 = agent2.choice(current_game)

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

print "Avg. and RbR Cooperation rates: laboritory VS simulation (learning rule: "+learning_rule+", game ID: "+str(game_ID)+")"
print

print "avg coop rates laboratory: \t", coop_avg
print "avg coop rates sim. of "+learning_rule+":\t", round(sum(sim_coop_rates)/len(sim_coop_rates),3)

print

print "RbR coop rates laboratory: \t",
if len(coop_rates) == 0:
    print "no data"
else:
    for rate in coop_rates:
        print round(rate, 3), "\t",
    print

print "RbR coop rates sim. of "+learning_rule+":\t",
for rate in sim_coop_rates:
    print round(rate,3), "\t",
print

