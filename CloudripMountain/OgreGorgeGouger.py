# https://codecombat.com/play/level/ogre-gorge-gouger?
# ¡Solo tenes 20 segundos hasta que llegue la horda de ogros!
# ¡Agarra tanto oro como puedas, luego retirate a tu base y amuralla!
while hero.time < 20:
    # Recoge las monedas
    item = hero.findNearestItem()
    hero.move(item.pos)
    
    
while hero.pos.x > 16:
    # Retirate detrás de la valla
    hero.say("Tengo que retirarme")
    hero.moveXY(14, 38) 
    
# Construye una valla para mantener a los ogros afuera.
hero.buildXY("fence", 21, 37)