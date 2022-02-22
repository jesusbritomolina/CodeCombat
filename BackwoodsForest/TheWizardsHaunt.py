# https://codecombat.com/play/level/the-wizards-haunt?
# Move to 'Zsofia' and get the secret number from her.
hero.moveXY(18, 20)
zso = hero.findNearestFriend().getSecret()

# Divide 'Zsofia's number by 4 to get 'Mihaly's number.
# Move to 'Mihaly' and say his magic number.
mih = zso / 4
hero.moveXY(30, 15)
hero.say(mih)

# Divide 'Mihaly's number by 5 to get 'Beata's number
# Move to 'Beata' and say her magic number.
beat = mih / 5
hero.moveXY(42, 20)
hero.say(beat)
# Subtract 'Beata's number from 'Mihaly's to get Sandor's number.
# Move to 'Sandor' and say his magic number.
sand = mih - beat
hero.moveXY(38, 37)
hero.say(sand)