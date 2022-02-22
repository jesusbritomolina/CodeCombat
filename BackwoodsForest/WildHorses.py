# https://codecombat.com/play/level/wild-horses?
while True:
    # How do you find the nearest friendly unit?
    # horse = ?
    horse = hero.findNearest(hero.findFriends())
    if horse:
        x1 = horse.pos.x - 7
        x2 = horse.pos.x + 7
        
        if x1 >= 1:
            # Move to the horse's y position but use x1 for the x position.
            hero.moveXY(x1,horse.pos.y)
        elif x2 <= 79:
            # Move to the horse's y position but use x2 for the x position.
            hero.moveXY(x2,horse.pos.y)
        distance = hero.distanceTo(horse)
        if distance <= 10:
            hero.say("Whoa")
            # Move to the red x to return the horse to the farm.
            hero.moveXY(27,54)
            # Move back out into the pasture to begin looking for the next horse.
            hero.moveXY(43,33)