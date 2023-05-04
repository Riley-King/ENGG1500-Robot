# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


hallway_top_path = []
hallway_top_walls = []

# Path
hallway_top_path.append(createAABB(1578, 0, 152, 715))

# Wall
hallway_top_walls.append(createAABB(300, 328, 187, 2018))
hallway_top_walls.append(createAABB(2826, 328, 188, 2017))
