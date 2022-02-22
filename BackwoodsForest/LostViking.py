# https://codecombat.com/play/level/lost-viking?
# You MUST click on the HELP button to see a detailed description of this level!

# The raven will tell you what to use for your maze parameters!
SLIDE=8
SWITCH=6
SKIP=11
sidemove = 1
# How many sideSteps north of the Red X you've taken.
sideSteps = 1

# How many steps east of the Red X you've taken.
steps = 1

# Multiply this with steps to determine your X coordinate. DON'T CHANGE THIS!
X_PACE_LENGTH = 4

# Multiply this with sideSteps to determine your Y coordinate. DON'T CHANGE THIS!
Y_PACE_LENGTH = 6

# The maze is 35 steps along the X axis.
while steps <= 35:

    # Take the next step:
    hero.moveXY(steps * X_PACE_LENGTH, sideSteps * Y_PACE_LENGTH)
    if (steps % SWITCH == 0):
        sidemove *= -1
    sideSteps += sidemove
    if (steps % SKIP == 0):
        sideSteps += sidemove
    if (sideSteps > SLIDE):
        sideSteps -= SLIDE
    if (sideSteps < 1):
        sideSteps += SLIDE
    # Increment steps and sideSteps as appropriate, taking into account the special rules.
    steps += 1