# https://codecombat.com/play/level/agony-of-defeat?
# El evento "defeat" indica que una unidad fue derrotada.
game.spawnPlayerXY("captain", 40, 35)
game.addSurviveGoal()
game.addCollectGoal(8)

def onSpawn(event):
    while True:
        unit = event.target
        enemy = unit.findNearestEnemy()
        if enemy:
            unit.attack(enemy)

# Cuando una unidad es derrotada, genera una moneda de oro.
def onDefeat(event):
    unit = event.target
    # Establezca x en unit.pos.x, más un número aleatorio entre -5 y 5
    x = unit.pos.x + game.randomInteger(-5, 5)
    # Establezca y en unit.pos.y, más un número entre -5 y 5
    y = unit.pos.y + game.randomInteger(-5, 5)
    # Genera una "gold-coin" (moneda de oro) en x, y
    game.spawnXY("gold-coin", 36, 30)

game.setActionFor("munchkin", "spawn", onSpawn)
game.setActionFor("munchkin", "defeat", onDefeat)

spawnTime = 0
while True:
    if game.time > spawnTime:
        x = game.randomInteger(10, 70)
        y = game.randomInteger(10, 60)
        game.spawnXY("munchkin", x, y)
        spawnTime = game.time + game.randomInteger(1,4)