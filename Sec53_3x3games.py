### IMPORTS ###

from Game import *
import Database.ExtendedGame as SDB
import MyMath as mYm
#import extFunc as eXf

### SET PARAMETERS ###

# choose set of learning rules from "CF", "EWA", "FP", "FWC", "NE", "RL"
learning_rules = ["FWC","EWA", "FP", "RL", "NE", "CF"]

# choose game by IDs for all SH games in the DB
game_IDs = [1, 2, 3, 4]

# choose the number of repetitions of the simulation
num_trials = 1000

print "mean square error values (Q2) for each game and averaged over all four games:"
print


# print the header
print "ALG",
for entry in game_IDs:
    print "\tGame", entry,
print "\tAVG"

# array for all lab cooperation rates
lab_coop_rates = []

# run through all learning rules and games
for learning_rule in learning_rules:

    print learning_rule, "  ",

    # array for simulated cooperation rates for all considered games
    sim_avg_rates = []

    avg_Q2 = 0.0

    for game_ID in game_IDs:

        ### INITIALISE THE SIMULATION EXPERIMENT ###

        # read data from the database SDB
        game_payoffs = SDB.BigGameDB[game_ID-1][1]
        game_type = SDB.BigGameDB[game_ID-1][2]
        coop_avg = SDB.BigGameDB[game_ID-1][3]
        num_rounds = SDB.BigGameDB[game_ID-1][4]
        num_agents = SDB.BigGameDB[game_ID-1][6]
        coop_rates = SDB.BigGameDB[game_ID-1][8]

        # initialize the game under investigation
        current_game = Game(game_type, game_payoffs)

        # compute the average coop rates over the number of trials for the current game
        sim_coop_RbR = mYm.simulate_avg3x3(current_game, num_agents, learning_rule, num_rounds, num_trials)

        Q2 = 0.0

        for index in range(len(sim_coop_RbR)):

            Q2 += (mYm.mean_square_error(sim_coop_RbR[index], coop_rates[index])/len(sim_coop_RbR))

        print "\t", str(round(Q2,4)),
        avg_Q2 += Q2/len(game_IDs)

    print "\t",round(avg_Q2,4)