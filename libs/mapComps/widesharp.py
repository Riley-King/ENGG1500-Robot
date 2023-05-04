# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])

widesharp_path = []
widesharp_walls = []

# Path
widesharp_path.append(createAABB(1580, 15, 152, 975))
widesharp_path.append(createAABB(1337, 778, 242, 436))
widesharp_path.append(createAABB(1108, 1001, 231, 444))
widesharp_path.append(createAABB(865, 1227, 246, 565))
widesharp_path.append(createAABB(468, 2576, 149, 721))
widesharp_path.append(createAABB(479, 1976, 294, 596))
widesharp_path.append(createAABB(612, 1506, 250, 469))
# Walls
