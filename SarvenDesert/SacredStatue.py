# https://codecombat.com/play/level/sacred-statue?
# Walk to a few points around the ogre camps, defeating any enemies along the way.
# Visit the statue to begin the event.
# Stand your ground and defeat the attacking ogres.

# Hint: fight close to the statue for it's assistance during the battle.
while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        hero.attack(enemy)
# After you defeat all of the waves, you will have to face off against the Ancient Cyclops!