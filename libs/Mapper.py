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

# 1 map px -> 23.4857 comp px
# 1px -> 2.02mm
def _pxTomm(px):
    return 2.0270714285714285714285714285714 * px
def _mmTopx(mm):
    return mm / 2.0270714285714285714285714285714
def _joinComp(a : list, b : list, b_x : float, b_y : float):
    for i in b:
        j = i.copy()
        j.x += b_x
        j.y += b_y
        a.append(j)

# TODO: Flip collider in either x- or y- axis. 1's bit means x-axis, 2's bit means y-axis. Should be in Mapper...
def flip(AABB):
    return AABB
class Mapper:
    def __init__(self):
        self.collider = AABB(0,0,0,0)
        self.map = []
        self.indexToName = {}
        #                                         TODO,     TODO,
        # Build map         [x_offset,  y_offset, Flip, Rotation,   path_AABB_list        , wall_AABB_list        , label]
        # Garage
        self.addMapComponent(-4      ,  8       , 0,           0,   _garage_left_path     , _garage_left_walls    , "Garage_l"   )
        self.addMapComponent(94      ,  8       , 0,           0,   _garage_right_path    , _garage_right_walls   , "Garage_r"   )
        self.addMapComponent(188     ,  6       , 0,           0,   _straightline_path    , _straightline_walls   , "Garage_str" )
        self.addMapComponent(269     ,  70      , 0,           1,   _gentle_turn_path     , _gentle_turn_walls    , "Garage_turn")
        self.addMapComponent(309     ,  172     , 0,           1,   _straightline_path    , _straightline_walls   , "Garage_up"  )

        self.addMapComponent(329     ,  259     , 0,           0,   _roundabout_path      , _roundabout_walls     , "round1"   )
        # First roundabout - west exit
        self.addMapComponent(227     ,  259     , 0,           0,   _straightline_path    , _straightline_walls   , "round1_w1")
        self.addMapComponent(122     ,  265     , 1,           1,   _distract_path        , _distract_walls       , "round1_w2")
        self.addMapComponent(17      ,  259     , 0,           2,   _sharp_turn_path      , _sharp_turn_walls     , "round1_w3")
        self.addMapComponent(-5      ,  345     , 0,           0,   _widesharp_path       , _widesharp_walls      , "round1_w4")
        self.addMapComponent(-51     ,  489     , 0,           1,   _straightline_path    , _straightline_walls   , "round1_w5")
        self.addMapComponent(-7      ,  590     , 2,           0,   _widesharp_path       , _widesharp_walls      , "round1_w6")
        self.addMapComponent(15      ,  677     , 0,           3,   _fork_path            , _fork_walls           , "round1_w7")
        # First roundabout - south exit
        self.addMapComponent(316     ,  384     , 0,           0,   _distract_path        , _distract_walls       , "round1_s1"   )
        self.addMapComponent(311     ,  485     , 0,           2,   _fork_path            , _fork_walls           , "round1_s1"   )
        self.addMapComponent(224     ,  506     , 0,           0,   _gentle_turn_path     , _gentle_turn_walls    , "round1_s1_w1")
        self.addMapComponent(204     ,  651     , 0,           3,   _gentle_turn_path     , _gentle_turn_walls    , "round1_s1_w2")
        self.addMapComponent(413     ,  484     , 2,           1,   _deadend_path         , _deadend_walls        , "round1_s1_e1")
        self.addMapComponent(423     ,  590     , 0,           0,   _distract_path        , _distract_walls       , "round1_s1_e2")
        self.addMapComponent(436     ,  674     , 3,           0,   _curve2021_path       , _curve2021_walls      , "round1_s1_e3")
        self.addMapComponent(311     ,  698     , 0,           0,   _fork_path            , _fork_walls           , "round1_s1"   )
        self.addMapComponent(310     ,  798     , 0,           1,   _straightline_path    , _straightline_walls   , "")
        # First roundabout - east exit
        self.addMapComponent(436     ,  260     , 0,           0,   _straightline_path    , _straightline_walls   , "round1_e1")
        self.addMapComponent(541     ,  256     , 0,           1,   _hallway_bottom_path  , _hallway_bottom_walls , "round1_e2")
        self.addMapComponent(641     ,  256     , 0,           1,   _hallway_top_path     , _hallway_top_walls    , "round1_e3")

        self.addMapComponent(747     ,  258     , 0,           0,   _roundabout_path      , _roundabout_walls     , "round2")
        # Second roundabout - north + east exits
        self.addMapComponent(852     ,  258     , 0,           0,   _sharp_turn_path      , _sharp_turn_walls     , "round2_e")
        self.addMapComponent(831     ,  173     , 0,           3,   _sharp_turn_path      , _sharp_turn_walls     , "round2_ne")
        self.addMapComponent(749     ,  153     , 0,           2,   _sharp_turn_path      , _sharp_turn_walls     , "round2_n")
        # Second roundabout - south exit
        self.addMapComponent(727     ,  427     , 0,           0,   _hallway_top_path     , _hallway_top_walls    , "round2_s1")
        self.addMapComponent(726     ,  525     , 0,           0,   _hallway_bottom_path  , _hallway_bottom_walls , "round2_s2")
        self.addMapComponent(726     ,  625     , 0,           0,   _converge_top_path    , _converge_top_walls   , "round2_s3")
        self.addMapComponent(726     ,  720     , 0,           0,   _converge_bottom_path , _converge_bottom_walls, "round2_s4")
        self.addMapComponent(727     ,  818     , 0,           1,   _straightline_path    , _straightline_walls   , "round2_s5")
        self.addMapComponent(744     ,  884     , 0,           0,   _sharp_turn_path      , _sharp_turn_walls     , "round2_s6")
        self.addMapComponent(642     ,  881     , 0,           1,   _hallway_top_path     , _hallway_top_walls    , "round2_s7")
        self.addMapComponent(543     ,  881     , 0,           1,   _hallway_bottom_path  , _hallway_bottom_walls , "round2_s8")
        self.addMapComponent(443     ,  883     , 0,           0,   _straightline_path    , _straightline_walls   , "round2_s9")

        self.addMapComponent(331     ,  885     , 0,           0,   _roundabout_path      , _roundabout_walls     , "round3")
        # Third roundabout - south exit
        self.addMapComponent(310     ,  1007    , 1,           1,   _deadend_path         , _deadend_walls        , "round3_s1")
        self.addMapComponent(429     ,  987     , 0,           0,   _sharp_turn_path      , _sharp_turn_walls     , "round3_s2")
        # Third roundabout - west exit
        self.addMapComponent(232     ,  884     , 0,           0,   _straightline_path    , _straightline_walls   , "round3_w1")
        self.addMapComponent(100     ,  907     , 0,           1,   _sharp_turn_path      , _sharp_turn_walls     , "round3_w2")
        self.addMapComponent(120     ,  784     , 0,           1,   _fork_path            , _fork_walls           , "round3_w3")
        self.addMapComponent(-3      ,  802     , 0,           1,   _sharp_turn_path      , _sharp_turn_walls     , "round3_w4")

        self.addMapComponent(119     ,  679     , 0,           0,   _roundabout_path      , _roundabout_walls     , "round4")
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
    def addMapComponent(self, x_offset : float, y_offset : float, f : int, rotation : int, path_AABB, wall_AABB, label):
        x_offset = _pxTomm(x_offset)
        y_offset = _pxTomm(y_offset)

        path = []
        for i in path_AABB:
            path.append(flip(i.copy(), f).rotate90(rotation).offsetPos(x_offset, y_offset))

        wall = []
        for i in wall_AABB:
            wall.append(flip(i.copy(), f).rotate90(rotation).offsetPos(x_offset, y_offset))

        # Append the component to the map with its paths, walls and label
        self.map.append([path, wall, label])


