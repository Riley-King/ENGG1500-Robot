# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])

deadend_path = []
deadend_walls = []

# Path
deadend_path.append(createAABB(1282, 922, 900, 378))
deadend_path.append(createAABB(1056, 1131, 223, 1682))
deadend_path.append(createAABB(0, 1424, 697, 329))
deadend_path.append(createAABB(697, 1246, 359, 343))
# Walls
deadend_walls.append(createAABB(2180, 0, 160, 2336))
