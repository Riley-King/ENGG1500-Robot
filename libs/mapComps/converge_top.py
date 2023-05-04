# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])

converge_top_path = []
converge_top_walls = []

# Path
converge_top_path.append(createAABB(1580, 0, 149, 924))
# Walls
# Left wall
converge_top_walls.append(createAABB(178, 1586, 312, 752))
converge_top_walls.append(createAABB(73, 1051, 268, 535))
converge_top_walls.append(createAABB(0, 315, 235, 737))
# Right wall
converge_top_walls.append(createAABB(2818, 1598, 310, 741))
converge_top_walls.append(createAABB(2968, 930, 293, 669))
converge_top_walls.append(createAABB(3103, 321, 208, 611))
