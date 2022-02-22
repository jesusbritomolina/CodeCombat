# https://codecombat.com/play/level/slumbering-sample?
# One last stop before the plan can be set into motion!
# It's up to you to help Senick get the average size of these yetis.

def average(array):
    sum = 0
    len = 0
    for yet in array:
        if yet.type == 'yeti':
            sum += yet.size
            len += 1
    return sum / len
# Find all the Yetis using 'findByType':
# Implement the averageSize function from scratch:
# Say the average size of the yetis:
enemies = hero.findEnemies()
hero.say(average(enemies))