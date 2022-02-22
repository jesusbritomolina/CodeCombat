# https://codecombat.com/play/level/pet-quiz?
# Write an event handler function called onHear

# Complete the onHear function
def onHear(event):
    # The pet should say something in onHear.
    pet.say("Hi")
    pass

pet.on("hear", onHear)

hero.say("Do you understand me?")
hero.say("Are you a cougar?")
hero.say("How old are you?")
# Ask two more questions.
hero.say("What day is it today?")
hero.say("How do you feel")