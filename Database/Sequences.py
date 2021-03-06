### Sequences of the Multi Game Environment Experiments ###



# Sequence of experiments by Schmidt et al. (2001)
SQ1 = [
    [[80,10],[110,40]], [[70,10],[110,50]], [[90,10],[110,50]], [[80,10],[110,60]],
    [[70,10],[110,30]], [[60,10],[110,40]], [[80,10],[110,40]], [[70,10],[110,50]],
    [[90,10],[110,50]], [[80,10],[110,60]], [[70,10],[110,30]], [[60,10],[110,40]],
    [[80,10],[110,40]], [[70,10],[110,50]], [[90,10],[110,50]], [[80,10],[110,60]],
    [[70,10],[110,30]], [[60,10],[110,40]], [[80,10],[110,40]], [[70,10],[110,50]],
    [[90,10],[110,50]], [[80,10],[110,60]], [[70,10],[110,30]], [[60,10],[110,40]]
]

# Resulting data for SQ1 experiments: average round-by-round cooperation rates
SQ1_data = [0.396,0.20825,0.22925,0.125,0.27075,0.104,0.125,0.0,
            0.20825,0.0625,0.25,0.0625,0.22925,0.12475,0.396,0.06225,
            0.271,0.0415,0.08325,0.0415,0.0835,0.0415,0.14575,0.02075]



# Sequence of Rankin et al. (2000)
SQ2 = [
    [[376,6],[299,299]],  [[415,45],[57,57]],   [[376,6],[313,313]],  [[407,37],[57,57]],
    [[417,47],[415,415]], [[392,22],[149,149]], [[411,41],[256,256]], [[372,2],[356,356]],
    [[418,48],[242,242]], [[389,19],[175,175]], [[412,42],[108,108]], [[371,1],[138,138]],
    [[388,18],[229,229]], [[404,34],[84,84]],   [[397,27],[225,225]], [[400,30],[173,173]],
    [[419,49],[62,62]],   [[408,38],[315,315]], [[370,0],[112,112]],  [[379,9],[330,330]],
    [[407,37],[377,377]], [[405,35],[388,388]], [[402,32],[320,320]], [[419,49],[309,309]],
    [[399,29],[77,77]],   [[390,20],[247,247]], [[401,31],[234,234]], [[373,3],[114,114]],
    [[398,28],[117,117]], [[384,14],[235,235]], [[376,6],[322,322]],  [[401,31],[85,85]],
    [[419,49],[237,237]], [[400,30],[309,309]], [[419,49],[134,134]], [[388,18],[269,269]],
    [[416,46],[300,300]], [[377,7],[186,186]],  [[402,32],[96,96]],   [[401,31],[120,120]],
    [[370,0],[305,305]],  [[399,29],[38,38]],   [[416,46],[190,190]], [[390,20],[167,167]],
    [[377,7],[287,287]],  [[386,16],[348,348]], [[384,14],[165,165]], [[396,26],[195,195]],
    [[394,24],[156,156]], [[379,9],[252,252]],  [[373,3],[17,17]],    [[379,9],[150,150]],
    [[414,44],[145,145]], [[393,23],[145,145]], [[370,0],[199,199]],  [[392,22],[372,372]],
    [[419,49],[157,157]], [[417,47],[307,307]], [[391,21],[374,374]], [[391,21],[175,175]],
    [[412,42],[400,400]], [[389,19],[366,366]], [[404,34],[207,207]], [[378,8],[171,171]],
    [[402,32],[283,283]], [[372,2],[201,201]],  [[412,42],[109,109]], [[409,39],[259,259]],
    [[382,12],[297,297]], [[404,34],[103,103]], [[407,37],[150,150]], [[395,25],[106,106]],
    [[381,11],[367,367]], [[400,30],[231,231]], [[415,45],[67,67]]
]

# Resulting data for SQ2 experiments by Rankin et al. (2000):
# average cooperation rates over the first 10 rounds [x < 0.5, x > 0.5] and the last 10 rounds [x < 0.5, x > 0.5]
SQ2_data = [0.71, [0.84,0.63], 0.96, [1.0,0.91] ]



# Sequences 3 to 6 of Ahn et al (2001)
SQ3 = [
    [[100,20],[60,60]],  [[100,20],[60,60]],  [[100,20],[60,60]],  [[100,20],[60,60]],
    [[100,20],[60,60]],  [[100,20],[60,60]],  [[100,20],[60,60]],  [[100,20],[60,60]],
    [[100,50],[110,60]], [[100,20],[110,60]], [[100,50],[140,60]], [[100,20],[140,60]]
]

# Resulting data for SQ4 experiments: average cooperation rates over 4 PD games
SQ3_data = [0.4, 0.275, 0.225, 0.275]


SQ4 = [
    [[100,20],[80,80]],  [[100,20],[80,80]],  [[100,20],[80,80]],  [[100,20],[80,80]],
    [[100,20],[80,80]],  [[100,20],[80,80]],  [[100,20],[80,80]],  [[100,20],[80,80]],
    [[100,50],[110,60]], [[100,20],[110,60]], [[100,50],[140,60]], [[100,20],[140,60]]
]

# Resulting data for SQ5 experiments: average cooperation rates over 4 PD games
SQ4_data = [0.45, 0.25, 0.325, 0.325]


SQ5= [
    [[100,60],[80,80]],  [[100,60],[80,80]],  [[100,60],[80,80]],  [[100,60],[80,80]],
    [[100,60],[80,80]],  [[100,60],[80,80]],  [[100,60],[80,80]],  [[100,60],[80,80]],
    [[100,50],[110,60]], [[100,20],[110,60]], [[100,50],[140,60]], [[100,20],[140,60]]
]

# Resulting data for SQ6 experiments: average cooperation rates over 4 PD games
SQ5_data = [0.45, 0.45, 0.325, 0.375]


SQ6 = [
    [[100,0],[80,60]],   [[100,0],[80,60]],   [[100,0],[80,60]],   [[100,0],[80,60]],
    [[100,0],[80,60]],   [[100,0],[80,60]],   [[100,0],[80,60]],   [[100,0],[80,60]],
    [[100,50],[110,60]], [[100,20],[110,60]], [[100,50],[140,60]], [[100,20],[140,60]]
]

# Resulting data for SQ7 experiments: average cooperation rates over 4 PD games
SQ6_data = [0.325, 0.25, 0.15, 0.2]
