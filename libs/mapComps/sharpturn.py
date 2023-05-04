# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


sharp_turn_path = []
sharp_turn_walls = []


sharp_turn_path.append(createAABB(1093, 483, 151, 1245))
sharp_turn_path.append(createAABB(0, 1579, 1094, 150))
