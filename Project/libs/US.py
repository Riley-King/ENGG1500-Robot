import ultrasonicLib
US = ultrasonicLib.sonic(17, 18)

def dist_mm():
    return US.distance_mm()
def getDist_mm():
    return US.distance_mm()