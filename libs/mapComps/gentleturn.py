# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


gentle_turn_path = []
gentle_turn_walls = []

# Path
gentle_turn_path.append(createAABB(1515, 645, 825, 316))
gentle_turn_path.append(createAABB(786, 799, 730, 483))
gentle_turn_path.append(createAABB(455, 1283, 549, 424))
gentle_turn_path.append(createAABB(163, 1706, 470, 1149))
# Walls
