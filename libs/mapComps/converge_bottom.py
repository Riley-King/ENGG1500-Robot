# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


converge_bottom_path = []
converge_bottom_walls = []
# Bottom-Central Black Line
converge_bottom_path.append(createAABB(1578, 1621, 150, 717))
# Left Wall
converge_bottom_walls.append(createAABB(329, 0, 267, 540))
converge_bottom_walls.append(createAABB(438, 540, 267, 540))
converge_bottom_walls.append(createAABB(545, 1083, 267, 540))
converge_bottom_walls.append(createAABB(654, 1622, 221, 336))
# Right Wall
converge_bottom_walls.append(createAABB(2711, 0, 267, 540))
converge_bottom_walls.append(createAABB(2604, 539, 267, 540))
converge_bottom_walls.append(createAABB(2498, 1079, 267, 540))
converge_bottom_walls.append(createAABB(2434, 1617, 244, 341))
