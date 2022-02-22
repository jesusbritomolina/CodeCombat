# https://codecombat.com/play/level/pet-translator?
# Your pet should translate commands.
 
def onHear(event):
    # The message the pet heard is in event.message
    message = event.message
    # If the message is "North":
    if message == "North":
        # The pet says "Htron".
        pet.say("Htron")
    # If the message is "South":
    if message == "South":
        # The pet says "Htuos".
        pet.say("Htuos")
        pass
    # If the message is "East":
    if message == "East":
        # The pet says "Tsae".
        pet.say("Tsae")

# Assign the event handler.
pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    # Don't attack Brawlers.
    if enemy and enemy.type != "brawler":
        hero.attack(enemy)
    else:
        hero.moveXY(26, 26)