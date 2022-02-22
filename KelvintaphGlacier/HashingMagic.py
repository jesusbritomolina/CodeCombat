# https://codecombat.com/play/level/hashing-magic?
# Use the hash function to find places for soldiers.
totalCells = 135

# This function hashes a string value to an integer.
def hashName(name):
    hash = 0
    for i in range(len(name)):
        letter = name[i]
        hash += ord(letter)
    # The hash value should be from 0 to 134.
    # Use modulo operation to "cut" the hash value.
    return hash%totalCells

soldiers = hero.findByType("soldier")
# For each soldier say his/her name (id) and hash of it.
# The name and the number should be splitted by whitespace.
for soldier in soldiers:
    hero.say(soldier.id +' '+hashName(soldier.id))