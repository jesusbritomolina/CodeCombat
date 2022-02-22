# # You can define the inner field.
# 1 is a peasant, 0 is an empty cell.
innerField = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]

hero.findNearestEnemy().initField(innerField)
while True:
    hero.wait(60)