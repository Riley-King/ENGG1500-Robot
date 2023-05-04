# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


distract_path = []
distract_walls = []

# Path
distract_path.append(createAABB(1424, 0, 152, 2340))
# Decoy paths
distract_path.append(createAABB(1574, 123, 942, 80))
distract_path.append(createAABB(480, 992, 945, 80))
distract_path.append(createAABB(1577, 2133, 942, 80))

# Walls
