# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


garage_left_path = []
garage_left_walls = []

# Path

# Walls
garage_left_walls.append(createAABB(143, 109, 2178, 195))
garage_left_walls.append(createAABB(140, 302, 194, 2878))
garage_left_walls.append(createAABB(334, 2984, 1985, 195))
