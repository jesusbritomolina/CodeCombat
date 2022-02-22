# https://codecombat.com/play/level/while-ogres-were-sleeping?
# Enemies are sleeping. It's the perfect time for sabotage!
points = [{"x": 21, "y": 8}, {"x": 33, "y": 8},
    {"x": 45, "y": 8}, {"x": 57, "y": 8}, {"x": 68, "y": 8},
    {"x": 68, "y": 18}, {"x": 68, "y": 28}, 
    {"x": 68, "y": 38}, {"x": 68, "y": 48},
    {"x": 68, "y": 58}, {"x": 56, "y": 58},
    {"x": 44, "y": 58}, {"x": 32, "y": 58}, 
    {"x": 20, "y": 58}, {"x": 10, "y": 60}]

pointIndex = 0;

while pointIndex < len(points):
    point = points[pointIndex];
    hero.moveXY(point["x"], point["y"])
    enemy = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    # Attack only if the enemy.team is "ogres"
    # AND the enemy's health is less than 10
    if enemy.team == "ogres" and enemy.health < 10:
        hero.attack(enemy)
    # Collect a coin if coin.value is less than 5
    # AND its distance is less than 7
    elif coin.value < 5 and hero.distanceTo(coin) < 7:
        hero.moveXY(coin.pos.x, coin.pos.y)
    # Attack only if the enemy.health is less than 10
    # AND the enemy's type is "skeleton".
    elif enemy.health < 10 and enemy.type == "skeleton":
        hero.attack(enemy)
    pointIndex += 1