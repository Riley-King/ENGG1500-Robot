# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])


roundabout_path = []
roundabout_walls = []

# Roundabout entrances
roundabout_path.append(createAABB(1094, 432, 148, 448))
roundabout_path.append(createAABB(1094, 2385, 151, 486))
roundabout_path.append(createAABB(0, 1580, 437, 151))
roundabout_path.append(createAABB(1900, 1580, 438, 150))

# Circle
# Top-Right
roundabout_path.append(createAABB(1245, 771, 324, 263))
roundabout_path.append(createAABB(1569, 864, 310, 259))
roundabout_path.append(createAABB(1682, 1123, 372, 457))
# Bottom-Right
roundabout_path.append(createAABB(1684, 1728, 370, 455))
roundabout_path.append(createAABB(1562, 2184, 319, 266))
roundabout_path.append(createAABB(1245, 2277, 318, 259))
# Top-Left
roundabout_path.append(createAABB(775, 772, 323, 263))
roundabout_path.append(createAABB(851, 861, 325, 274))
roundabout_path.append(createAABB(288, 1133, 362, 447))
# Bottom-Left
roundabout_path.append(createAABB(287, 1728, 365, 448))
roundabout_path.append(createAABB(779, 2278, 318, 261))
roundabout_path.append(createAABB(452, 2175, 328, 273))
