# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])

fork_path = []
fork_walls = []

# Path
fork_path.append(createAABB(1574, 1987, 154, 352))
fork_path.append(createAABB(483, 1095, 702, 274))
fork_path.append(createAABB(2128, 1091, 697, 272))
fork_path.append(createAABB(1186, 1191, 944, 795))
# Walls
