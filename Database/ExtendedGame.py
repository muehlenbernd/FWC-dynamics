### Database for Extended Game Experiment ###

import Rates_3x3 as r3x3

# Each line contains the following information for a single game experiment:
# 1. ID
# 2. game payoffs
# 3. game type
# 4. average cooperation rate over all trials, rounds and participants
# 5. number of rounds per trial
# 6. number of trials
# 7. number of participants per trial
# 8. Source literature
# 9. round-by-round cooperation rates (or block-by-block cooperation rates for some chicken games)
#    Rates for 3x3 games (of playing H, M or L) are imported from file Rates_3x3

ChickenGameDB=[
[   1, [[200,100],[300,0]], 'CH', 0.477, 12, 8, 6, "Kuemmerli et al. 2007",
  [0.75,0.646,0.458,0.396,0.396,0.333,0.563,0.542,0.417,0.396,0.396,0.438], 1],
[   2, [[2,2],[5,0]], 'CH', 0.431, 40, 1, 20, "Bornstein et al. 2007",
  [0.34,0.395,0.47,0.52], 10],
[   3, [[7,3],[9,0]], 'CH', 0.596, 20, 16, 12, "Duffy & Feltovich 2010",
  [0.653, 0.587, 0.602,	0.543],5],
[   4, [[39,9],[48,3]], 'CH', 0.455, 60, 4, 12, "Cason & Sharma 2007",
  [0.57, 0.47, 0.43, 0.47, 0.43, 0.39],10],
[   5, [[160,80],[200,20]], 'CH', 0.562, 20, 6, 15, "Feltovich 2011",
  [0.675, 0.6, 0.675, 0.53, 0.6, 0.52, 0.635, 0.56, 0.54, 0.57, 0.5, 0.49, 0.56, 0.575, 0.52, 0.53, 0.51, 0.52, 0.56, 0.53],1],
[   6, [[120,40],[160,-20]], 'CH', 0.65, 20, 6, 15, "Feltovich 2011",
  [0.82, 0.75, 0.67, 0.725, 0.68, 0.625, 0.625, 0.6, 0.65, 0.64, 0.66, 0.59, 0.64, 0.63, 0.63, 0.61, 0.62, 0.61, 0.61, 0.57 ],1],
[    7, [[70,50],[80,40]], 'CH', 0.537, 10, 4, 20, "Duffy & Feltovich 2002",
          [0.5875,0.5,0.5875,0.575,0.4875,0.5125,0.5,0.475,0.5875,0.5625], 1] #47	40	47	46	39	41	40	38	47	45 of 80
]


BigGameDB = [
[ 1, [[350,350,1000],[250,550,0],[0,0,600]],  '3x3', [0.714, 0.2, 0.086],   22, 1, 10, "Cooper et al 1990", r3x3.Cooper3],
[ 2, [[350,350,700],[250,550,0],[0,0,600]],   '3x3', [0.709, 0.141, 0.150], 22, 1, 10, "Cooper et al 1990", r3x3.Cooper4],
[ 3, [[350,350,700],[250,550,1000],[0,0,600]],'3x3', [0.023, 0.918, 0.059], 22, 1, 10, "Cooper et al 1990", r3x3.Cooper5],
[ 4, [[350,350,700],[250,550,650],[0,0,600]], '3x3', [0.068, 0.786, 0.145], 22, 1, 10, "Cooper et al 1990", r3x3.Cooper6],
]
