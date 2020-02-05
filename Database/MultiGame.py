### Database for Multi Game Experiment ###

from Sequences import *

# Each line contains the following information for a single game experiment:
# 1. Experiment ID
# 2. Game sequence (import from file Sequences.py)
# 3. number of participants per trial
# 4. Source literature
# 5. Result data (import from file Sequences.py)
# 6. Description of result data



MultiGameDB=[
[ 1, SQ1,  8, "Schmidt et al. 2001",    SQ1_data,  "Round-by-Round Cooperation rates"],
[ 2, SQ2,  8, "Rankin et al. 2000",     SQ2_data, "Avg Coop. rates: first 10 round [x<0.5,x>0.5], last 10 rounds [x<0.5,x>0.5]"],
[ 5, SQ3, 10, "Ahn et al. 2001",        SQ3_data,  "Round-by-Round Cooperation rates over 4 PD games"],
[ 6, SQ4, 10, "Ahn et al. 2001",        SQ4_data,  "Round-by-Round Cooperation rates over 4 PD games"],
[ 7, SQ5, 10, "Ahn et al. 2001",        SQ5_data,  "Round-by-Round Cooperation rates over 4 PD games"],
[ 8, SQ6, 10, "Ahn et al. 2001",        SQ6_data,  "Round-by-Round Cooperation rates over 4 PD games"]
]
