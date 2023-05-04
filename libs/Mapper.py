from libs.AABB import AABB
from libs.mapComps.full_map import map, full_map_walls
# Import wall components
from libs.mapComps.fork import fork_path as _fork_path, fork_walls as _fork_walls
from libs.mapComps.converge_bottom import converge_bottom_path as _converge_bottom_path, converge_bottom_walls as _converge_bottom_walls
from libs.mapComps.hallway_bottom import hallway_bottom_path as _hallway_bottom_path, hallway_bottom_walls as _hallway_bottom_walls
from libs.mapComps.hallway_top import hallway_top_path as _hallway_top_path, hallway_top_walls as _hallway_top_walls
from libs.mapComps.converge_top import converge_top_path as _converge_top_path, converge_top_walls as _converge_top_walls
from libs.mapComps.curve2021 import curve2021_path as _curve2021_path, curve2021_walls as _curve2021_walls
from libs.mapComps.deadend import deadend_path as _deadend_path, deadend_walls as _deadend_walls
from libs.mapComps.distract import distract_path as _distract_path, distract_walls as _distract_walls
from libs.mapComps.garage_left import garage_left_path as _garage_left_path, garage_left_walls as _garage_left_walls
from libs.mapComps.garage_right import garage_right_path as _garage_right_path, garage_right_walls as _garage_right_walls
from libs.mapComps.gentleturn import gentle_turn_path as _gentle_turn_path, gentle_turn_walls as _gentle_turn_walls
from libs.mapComps.roundabout import roundabout_path as _roundabout_path, roundabout_walls as _roundabout_walls
from libs.mapComps.sharpturn import sharp_turn_path as _sharp_turn_path, sharp_turn_walls as _sharp_turn_walls
from libs.mapComps.straightline import straightline_path as _straightline_path, straightline_walls as _straightline_walls
from libs.mapComps.widesharp import widesharp_path as _widesharp_path, widesharp_walls as _widesharp_walls
def _joinComp(a : list, b : list, b_x : float, b_y : float):
    for i in b:
        j = i.copy()
        j.x += b_x
        j.y += b_y
        a.append(j)


class Mapper:
    def __init__(self):
        self.collider = AABB(0,0,0,0)
        self.map = []
        self.indexToName = {}

        # Build map         [x_offset,  y_offset,   path_AABB_list        , wall_AABB_list        , label]
        self.addMapComponent(0       ,  0       ,   _fork_path            , _fork_walls           , ""   )
        self.addMapComponent(0       ,  0       ,   _converge_bottom_path , _converge_bottom_walls, ""   )
        self.addMapComponent(0       ,  0       ,   _hallway_bottom_path  , _hallway_bottom_walls , ""   )
        self.addMapComponent(0       ,  0       ,   _hallway_top_path     , _hallway_top_walls    , ""   )
        self.addMapComponent(0       ,  0       ,   _converge_top_path    , _converge_top_walls   , ""   )
        self.addMapComponent(0       ,  0       ,   _curve2021_path       , _curve2021_walls      , ""   )
        self.addMapComponent(0       ,  0       ,   _deadend_path         , _deadend_walls        , ""   )
        self.addMapComponent(0       ,  0       ,   _distract_path        , _distract_walls       , ""   )
        self.addMapComponent(0       ,  0       ,   _garage_left_path     , _garage_left_walls    , ""   )
        self.addMapComponent(0       ,  0       ,   _garage_right_path    , _garage_right_walls   , ""   )
        self.addMapComponent(0       ,  0       ,   _gentle_turn_path     , _gentle_turn_walls    , ""   )
        self.addMapComponent(0       ,  0       ,   _roundabout_path      , _roundabout_walls     , ""   )
        self.addMapComponent(0       ,  0       ,   _sharp_turn_path      , _sharp_turn_walls     , ""   )
        self.addMapComponent(0       ,  0       ,   _straightline_path    , _straightline_walls   , ""   )
        self.addMapComponent(0       ,  0       ,   _widesharp_path       , _widesharp_walls      , ""   )

    def __index__(self, idx):
        return self.map[idx]
    def move(self, dx : float, dy : float):
        self.collider.x += dx
        self.collider.y += dy

    # Returns the indexes for map path components where they intersect with the collider
    def getPathIntersectionIndexes(self):
        paths = []
        for i, m in enumerate(map):
            if self.collider.doesIntersect(m[0]):
                paths.append(i)
        return paths
    # Returns the indexes for map wall components where they intersect with the collider
    def getWallIntersectionIndexes(self):
        walls = []
        for i, m in enumerate(map):
            if self.collider.doesIntersect(m[1]):
                walls.append(i)
        return walls
    def addMapComponent(self, x_offset : float, y_offset : float, path_AABB, wall_AABB, label):
        # Copy the collider and offset it according to the maps position
        path = path_AABB.copy().offsetPos(x_offset, y_offset)
        wall = wall_AABB.copy().offsetPos(x_offset, y_offset)
        # Append the component to the map with its paths walls and label
        self.map.append([path, wall, label])


