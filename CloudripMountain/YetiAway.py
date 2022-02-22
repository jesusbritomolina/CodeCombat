# https://codecombat.com/play/level/yeti-away?
# Follow one of the peasants and escape from the yeti.

def startsWith(phrase, word):
    if len(word) > len(phrase):
        return False
    # Iterate indexes from 0 to the length of the word.
    for i in range(len(word)):
        # Check the letter of phrase and word at index i
        # If they are not equal:
        if phrase[i] != word[i]:
            # Then return False.
            return False
    # All letters in the word checked, then return true.
    return True

# Follow the local guide whose name starts with "Mac".
guides = hero.findFriends()
for gIndex in range(len(guides)):
    guide = guides[gIndex]
    if startsWith(guide.id, "Mac"):
        while True:
            hero.move(guide.pos)