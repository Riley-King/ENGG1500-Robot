# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


hallway_bottom_path = []
hallway_bottom_walls = []

# Path
hallway_bottom_path.append(createAABB(1578, 1530, 151, 819))
# Walls
hallway_bottom_walls.append(createAABB(297, 0, 187, 1914))
hallway_bottom_walls.append(createAABB(2824, 0, 184, 1917))
