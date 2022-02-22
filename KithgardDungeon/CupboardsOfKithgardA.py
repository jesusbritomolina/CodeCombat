# https://codecombat.com/play/level/cupboards-of-kithgard-a?
# There may be something around to help you!

# First, move to the Cupboard.
hero.moveDown()
hero.moveLeft(2)

# Then, attack the "Cupboard" inside a while-true loop.
while True:
    hero.attack("Cupboard")