# https://codecombat.com/play/level/cloudrip-siege?
# Your goal is to keep at least one flower alive for 60 seconds.
# This is an optional challenge level, intended to be difficult. Be creative with your code!
# It gets harder (and more lucrative) each time you succeed. If you fail, you must wait a day to resubmit.
def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)


# pickup coin
def pickUpNearestItem():
    items = hero.findItems()
    nearestItem = hero.findNearest(items)
    if nearestItem:
        moveTo(nearestItem.pos)


# add soldier
coors = [[67, 41], [24, 54], [69, 55], [25, 34], [69, 32]]
buildTypes = ['arrow-tower']


def buildTroops():
    coor = coors[len(hero.built) % len(coors)]
    type = buildTypes[len(hero.built) % len(buildTypes)]
    if hero.gold > hero.costOf(type):
        hero.buildXY(type, coor[0], coor[1])


while True:
    pickUpNearestItem()
    buildTroops()