# https://codecombat.com/play/level/northwest?
# Your pet should find and then bring the potion to the hero.

# This function checks if the word is in the text.
def wordInText(text, word):
    # Iterate through each character in the text.
    for i in range(len(text) - len(word) + 1):
        # For each of them loop through each character in word.
        for j in range(len(word)):
            # Store the shifted index i + j.
            shiftedIndex = i + j
            # If a character within the shifted index.
            # isn't equal to the character in word at the index "j"
            if text[shiftedIndex] != word[j]:
                # Break the loop.
                break
            # If j is equal to the index of the last letter in word
            if shiftedIndex == len(text) - len(word) - 1:
                # Then the entire word is in the text.
                # Return True.
                return True
    # The word was not found in text. Return False.
    return False

# Follow the guides directions where to run.
def onHear(event):
    # If "west" is in the phrase, the pet should run left.
    if wordInText(event.message, "west"):
        pet.moveXY(pet.pos.x - 28, pet.pos.y)
    # If "north" is in the phrase, the pet should run up.
    elif wordInText(event.message, "north"):
        pet.moveXY(pet.pos.x, pet.pos.y + 24)
    # Else the pet should try to fetch the potion.
    else:
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)

pet.on("hear", onHear)