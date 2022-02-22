# https://codecombat.com/play/level/village-champion?
# Incoming munchkins! Defend the town!

# Define your own function to fight the enemy!
def cleaveOrAttack():
    # In the function, find an enemy, then cleave or attack it.
    ogre = hero.findNearestEnemy()
    if ogre:
        if hero.isReady("cleave"):
            hero.cleave(ogre)
        # Else attack the ogre:
        hero.attack(ogre)

# Move between patrol points and call the function.
while True:
    hero.moveXY(35, 34)
    # Use cleaveOrAttack function you defined above.
    cleaveOrAttack()
    hero.moveXY(47, 27)
    # Call the function again.
    cleaveOrAttack()
    hero.moveXY(60, 31)
    # Call the function again.
    cleaveOrAttack()