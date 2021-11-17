### IMPORTS ###

from LearningRules import *
from Game import *
import Database.AcrossGame as ADB
import MyMath as MyMath


### SET PARAMETERS ###

# choose learning rule from "CF", "EWA", "FP", "FWC", "NE", "RL"
learning_rule = "FWC"

# choose the number of repetitions of the simulation
num_trials = 10

# choose the ID (0, 1, 2 or 3) for the sequence of Duffy & Fehr 2018:
ID = 3

# choose if reset agents
Reset = False


###### set up the data ######

LAB_game1 = ADB.DuffyDB[ID][0]
LAB_game2 = ADB.DuffyDB[ID][1]
LAB_rates = ADB.DuffyDB[ID][2]
LAB_structure = ADB.DuffyDB[ID][3]

current_sequence = []

for dummy in range(LAB_structure[0]):
    current_sequence.append(LAB_game1)
for dummy in range(LAB_structure[1]):
    current_sequence.append(LAB_game2)
for dummy in range(LAB_structure[2]):
    current_sequence.append(LAB_game1)




### INITIALISE THE SIMULATION EXPERIMENT ###

# read data from the database MultiGameDB
num_agents = 10
source ="Duffy and Fehr 2018"


# initialize the sequence as an array of objects of the class Game
game_sequence = []
for game_payoffs in current_sequence:
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
        new_agent = FWC('new')
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
        current_game = game_sequence[current_round%len(game_sequence)]

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


        if current_round == LAB_structure[0]-1 or current_round == LAB_structure[0]+LAB_structure[1]-1:

            if Reset == True:

                for agent in agents:

                    agent.reset()

        # update the array that records rounds-by-round cooperation rates averaged over all agents and trials
        sim_coop_rates[current_round] += num_coop*1.0/(num_agents*num_trials)


### PRINT THE SIMULATION RESULTS ###
print "RbR coop rates sim. of "+learning_rule+":\t",
print
print "Round \texp rate\tsim rate"
entry_counter = 0
for index in range(len(sim_coop_rates)):

    exp_rate = LAB_rates[index]
    sim_rate = sim_coop_rates[index]

    print "  "+str(index+1)+" \t"+str(round(exp_rate,3))+"     \t"+str(round(sim_rate,3))

    entry_counter += 1

print


mse = 0.0
for index in range(len(sim_coop_rates)):

    sim_rate = sim_coop_rates[index]
    lab_rate = LAB_rates[index]

    mse += ((sim_rate-lab_rate)**2)

print "mean square error (Q2): ", mse/len(sim_coop_rates)