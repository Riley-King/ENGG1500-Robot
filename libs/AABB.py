class AABB:
    def __init__(self, x : float, y : float, width : float, height : float):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def offsetPos(self, x_ofst, y_ofst):
        self.x += x_ofst
        self.y += y_ofst
        return self
    def offsetSize(self, x_scale, y_scale):
        self.w += x_scale
        self.h += y_scale
        return self
    def area(self):
        return self.w*self.h
    def doesIntersect(self, other):
        return (self.x+self.w) >= other.x and (other.x+other.w) >= self.x and \
            (self.y+self.h) >= other.y and (other.y+other.h) >= self.y

    def __copy__(self):
        return AABB(self.x, self.y, self.w, self.h)

    # https://stackoverflow.com/q/25349178
    def intersects(self, other):
        if not self.doesIntersect(other): return False, 0.0, None

        x_left = 0
        x_right = 0
        y_top = 0
        y_bottom = 0

        if self.x >= other.x:
            x_left = self.x
            x_right = other.y
        else:
            x_left = other.x
            x_right = self.x

        if self.y >= other.y:
            y_top = self.y
            y_bottom = other.y
        else:
            y_top = other.y
            y_bottom = self.y

        if (x_right < x_left) or (y_bottom < y_top): return False, 0.0, None

        intAABB = AABB(x_left, y_top, x_right-x_left, y_bottom-y_top)
        return True, intAABB.area()/(self.area()+other.area()-intAABB.area()), intAABB
