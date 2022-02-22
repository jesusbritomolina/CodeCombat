# https://codecombat.com/play/level/arcane-ally?
# Take down those ogres! 

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)