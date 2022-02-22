# https://codecombat.com/play/level/gems-or-death?
# Los comandos debajo de un if solo corren cuando la condición es verdadera.
# Fix all the if-statements to beat the level.

# == significa "es igual a"
if 1 + 1 + 1 == 4:  # ∆ Haz que esto sea falso.
    hero.moveXY(5, 15)  # Muévete a las primeras minas.

if 2 + 2 == 4:  # ∆ Haz que esto sea verdadero.
	hero.moveXY(15, 40)  # Múevete hacia la primer gema.

# != significa "no es igual a"
if 2 + 2 != 3:  # ∆ Haz que esto sea verdadero.
	hero.moveXY(25, 15)  # Múevete hacia la segunda gema.
	
# < significa "menor a"
if 2 + 2 < 5:  # ∆ Haz que esto sea verdadero.
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

if 2 < 1:  # ∆ Haz que esto sea falso.
	hero.moveXY(40, 55)

if False:  # ∆ Haz que esto sea falso.
	hero.moveXY(50, 10)

if True:  # ∆ Haz que esto sea verdadero.
	hero.moveXY(55, 25)