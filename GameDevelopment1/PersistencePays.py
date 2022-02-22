# https://codecombat.com/play/level/persistence-pays?
# You can use a database to store persistent data.
# Persistent data stays the same between plays of your game!

generator = game.spawnXY("generator", 60, 40)
generator.spawnType = "munchkin"
generator.spawnDelay = 1
player = game.spawnPlayerXY("raider", 36, 30)
player.maxHealth = 70
player.attackDamage = 10
game.addSurviveGoal(8)

# db stands for database
# db.add(key, value) increments a value stored in the database.
# This adds 1 to the "plays" key in the database.
db.add("plays", 1)

# Show the value of the "plays" and other keys in the db
ui.track(db, "plays")
ui.track(db, "wins")
ui.track(db, "total defeated")

ui.track(game, "time")

# Show the value of the "defeated" property of the game object
ui.track(game, "defeated")
# The code below will run when the player wins the game.
def onVictory(event):
    db.add("wins", 1)
    # Use db.add(key, value) to add the value of
    # game.defeated to the database with the key "total defeated"
    db.add("total defeated", 2)

game.on("victory", onVictory)