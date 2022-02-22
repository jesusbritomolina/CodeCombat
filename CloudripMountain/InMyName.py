# https://codecombat.com/play/level/in-my-name?
# You must to find the treasure.

# This function should return the index of a letter:
def letterIndex(word, letter):
    # Step through each letter as an index of the word.
    for index in range(0, len(word), 1):
        # Store a character from the word with the current index.
        # If it is the required letter:
        if (word[index] == letter):
            # Then return the current index (number).
            return index
    # If nothing, return a default value
    return -1

ogreLetter = "z"
shaman = hero.findByType("thoktar")[0]

# Find the index and use it for finding the treasure.
chestIndex = letterIndex(shaman.id, ogreLetter)
hero.moveXY(16 + chestIndex * 8, 36)