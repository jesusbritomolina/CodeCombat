# https://codecombat.com/play/level/echo-of-war?
# Destroy 5 robobombs. Some of them are old and safe.
# Old (safe) bombs have the certain letter in their id.

# This function checks if searchLetter is in searchWord.
def isLetterInWord(searchWord, searchLetter):
    # Complete the function.
    for index in range(len(searchWord)):
        if searchWord[index] == searchLetter:
            return True
    return False

# The engineer knows how the old robots are marked.
engineer = hero.findFriends()[0]
safeLetter = engineer.safeLetter

enemies = hero.findEnemies()
for index in range(len(enemies)):
    enemy = enemies[index]
    if isLetterInWord(enemy.id, safeLetter):
        # Destroy the enemy if it's safe.
        while enemy.health > 0:
            hero.attack(enemy)