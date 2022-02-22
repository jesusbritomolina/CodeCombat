# https://codecombat.com/play/level/almost-perfect-minefield?
# Escape from the minefield.
# You need to pass the marked line. (x = 72).

trapDistance = 6
trapRange = 2

# Jump, Jump, JUMP!!!
hero.jumpTo({'x': 40, 'y': 10})
hero.jumpTo({'x': 34, 'y': 22})
hero.jumpTo({'x': 34, 'y': 34})
hero.jumpTo({'x': 22, 'y': 34})
hero.jumpTo({'x': 22, 'y': 46})
hero.jumpTo({'x': 22, 'y': 58})
hero.jumpTo({'x': 34, 'y': 58})
hero.jumpTo({'x': 46, 'y': 58})
hero.jumpTo({'x': 59, 'y': 58})
hero.jumpTo({'x': 72, 'y': 58})
hero.moveXY(72, 58)