# https://codecombat.com/play/level/razorfray?
# Use throwPos and removeFlag to throw where you aim flags.
# Defeat the ogres and purple cow, but not the ice yak.
# Target placement is random with each submission.

while True:
    flag = hero.findFlag()
    if flag:
        hero.throwPos(flag.pos)
        hero.removeFlag(flag)