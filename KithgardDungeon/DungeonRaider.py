# https://codecombat.com/play/level/dungeon-raider?
# Explore the dungeon, kill munchkins, and avoid any danger.
# Your goal is to find the treasure of Kithgard: The Holy Sword.
# This level uses a scrolling level mechanic. Check Hints for more information.
hero.moveUp(4)
hero.moveUp(2)
hero.moveRight(2)
hero.moveUp()
enemy = hero.findNearestEnemy()
hero.attack(enemy)
hero.attack(enemy)
hero.moveRight()
hero.moveDown(4)
hero.moveDown()
hero.moveRight(2)
enemy = hero.findNearestEnemy()
hero.attack(enemy)
hero.attack(enemy)
hero.attack(enemy)
hero.moveUp(2)
hero.moveUp(2)
enemy = hero.findNearestEnemy()
hero.attack(enemy)
hero.attack(enemy)
hero.moveRight()
hero.moveDown(4)
hero.moveDown()
hero.moveRight(2)