# https://codecombat.com/play/level/dance-off?
# Move in sync with your dance partner to impress Pender Spellbane.
nearest = hero.findNearest(hero.findFriends())

while True:
    hero.moveXY(nearest.pos.x, nearest.pos.y-5)