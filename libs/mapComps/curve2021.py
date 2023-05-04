# 150 px -> 15-25 mm (20 avg)
# 1 px -> 0.1-0.17 mm (0.13 avg)

from libs.AABB import AABB
conversionFactor = [0.1333, 0.1333]
def createAABB(px,py,pw,ph):
    return AABB(px*conversionFactor[0], py*conversionFactor[1], pw*conversionFactor[0], ph*conversionFactor[1])

curve2021_path = []
curve2021_walls = []

# Path
curve2021_path.append(createAABB(980, 2369, 264, 480))
curve2021_path.append(createAABB(757, 2152, 220, 443))
curve2021_path.append(createAABB(568, 2000, 192, 360))
curve2021_path.append(createAABB(409, 1832, 161, 351))
curve2021_path.append(createAABB(278, 1631, 134, 422))
curve2021_path.append(createAABB(80, 1537, 200, 368))
curve2021_path.append(createAABB(59, 752, 217, 786))
curve2021_path.append(createAABB(274, 590, 242, 429))
curve2021_path.append(createAABB(516, 543, 388, 212))
curve2021_path.append(createAABB(804, 565, 414, 308))
curve2021_path.append(createAABB(1134, 872, 413, 380))
curve2021_path.append(createAABB(1363, 1252, 365, 336))
curve2021_path.append(createAABB(1727, 1414, 614, 311))

# Walls
