# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


garage_right_path = []
garage_right_walls = []

# Path

# Walls
garage_right_walls.append(createAABB(0, 105, 968, 192))
garage_right_walls.append(createAABB(0, 2983, 970, 196))
