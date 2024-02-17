# create a Point class.
class Point:
    # parameterized constructor
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
    
    # customize the string representation of a Point class instance
    def __str__(self):
        return "({},{})".format(self.x_cord, self.y_cord)
    
    def __add__(self, other):
        # return a new Point object with the coordinates added
        new_x_cord = self.x_cord + other.x_cord
        new_y_cord = self.y_cord + other.y_cord
        return Point(new_x_cord, new_y_cord)

    # method to calculate distance between two points
    def distance(self, other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5
    
    # method to calculate distance from the origin
    def distance_from_origin(self):
        return self.distance(Point(0,0))


# create a line class
class Line:
    def __init__(self, A, B, C):
        self.a = A
        self.b = B
        self.c = C
    
    def __str__(self):
        return "{}x+{}y+{}=0".format(self.a, self.b, self.c)
    
    def slope(self):
        return -self.a / self.b
    
    def shortest_distance(self, point):
        return abs(self.a*point.x_cord + self.b*point.y_cord + self.c) / (self.a**2 + self.b**2)**0.5



# p1 = Point(0,1)
# p2 = Point(1,0)

# p1.distance_from_origin()

# l1 = Line(2,3,4)
# print(l1)

# l1.shortest_distance(p1)
