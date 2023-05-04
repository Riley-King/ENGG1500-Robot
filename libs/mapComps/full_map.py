from libs.mapComps.fork import fork_path, fork_walls
from libs.mapComps.converge_bottom import converge_bottom_path, converge_bottom_walls
from libs.mapComps.hallway_bottom import hallway_bottom_path, hallway_bottom_walls
from libs.mapComps.hallway_top import hallway_top_path, hallway_top_walls
from libs.mapComps.converge_top import converge_top_path, converge_top_walls
from libs.mapComps.curve2021 import curve2021_path, curve2021_walls
from libs.mapComps.deadend import deadend_path, deadend_walls
from libs.mapComps.distract import distract_path, distract_walls
from libs.mapComps.garage_left import garage_left_path, garage_left_walls
from libs.mapComps.garage_right import garage_right_path, garage_right_walls
from libs.mapComps.gentleturn import gentle_turn_path, gentle_turn_walls
from libs.mapComps.roundabout import roundabout_path, roundabout_walls
from libs.mapComps.sharpturn import sharp_turn_path, sharp_turn_walls
from libs.mapComps.straightline import straightline_path, straightline_walls
from libs.mapComps.widesharp import widesharp_path, widesharp_walls

def _joinComp(a : list, b : list, b_x : float, b_y : float):
    for i in b:
        j = i.copy()
        j.x += b_x
        j.y += b_y
        a.append(j)

map = []
full_map_walls = []

_joinComp(map, fork_path, 0, 0)
_joinComp(map, converge_bottom_path, 0, 0)
_joinComp(map, hallway_bottom_path, 0, 0)
_joinComp(map, hallway_top_path, 0, 0)
_joinComp(map, converge_top_path, 0, 0)
_joinComp(map, curve2021_path, 0, 0)
_joinComp(map, deadend_path, 0, 0)
_joinComp(map, distract_path, 0, 0)
_joinComp(map, garage_left_path, 0, 0)
_joinComp(map, garage_right_path, 0, 0)
_joinComp(map, gentle_turn_path, 0, 0)
_joinComp(map, roundabout_path, 0, 0)
_joinComp(map, sharp_turn_path, 0, 0)
_joinComp(map, straightline_path, 0, 0)
_joinComp(map, widesharp_path, 0, 0)
