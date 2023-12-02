# Written by *** for COMP9021
#
# Defines two classes, Point and Triangle.
#
# An object of class Point is created by passing exactly
# 2 integers as arguments to __init__().
# You can assume that nothing but integers will indeed be
# passed as arguments to __init__(), but not that exactly
# 2 arguments will be provided; when that is not the case,
# a PointError error is raised.
# The point class implements the __str__() and __repr__()
# special methods.
#
# An object of class Triangle is created by passing exactly
# 3 points as keyword only arguments to __init__().
# You can assume that exactly three points will indeed be
# passed as arguments to __init__().
# The three points should not be collinear for the triangle
# to be created; otherwise a TriangleError error is raised.
# A triangle object can be modified by changing one two or three
# points thanks to the method change_point_or_points(),
# all of whose arguments are keyword only.
# At any stage, the object maintains correct values
# for perimeter and area.


from math import sqrt


# INSERT YOUR CODE HERE

class PointError(Exception):
    pass


class TriangleError(Exception):
    pass


class Point:

    def __init__(self, *args):

        if len(args) != 2:
            raise PointError('Need two coordinates, point not created.')

        x, y = args

        if x is None or y is None:
            raise PointError('Need two coordinates, point not created.')

        # if not (x == int(x) and y == int(y)):
        if (not isinstance(x, int)) or (not isinstance(y, int)):
            raise PointError('Need two coordinates, point not created.')

        self.x = x
        self.y = y

    def __str__(self):
        return f'Point of x-coordinate {self.x} and y-coordinate {self.y}'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        # if (point_2.y - point_1.y) / (point_2.x - point_1.x) == \
        #         (point_3.y - point_1.y) / (point_3.x - point_1.x):
        if (point_2.y - point_1.y) * (point_3.x - point_1.x) == \
                (point_3.y - point_1.y) * (point_2.x - point_1.x):
            raise TriangleError('Incorrect input, triangle not created.')

        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

        self.perimeter = self.compute_perimeter()
        self.area = self.compute_area()

    # @property
    def compute_perimeter(self):
        A = self.point_1
        B = self.point_2
        C = self.point_3

        AB = sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
        BC = sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)
        AC = sqrt((C.x - A.x) ** 2 + (C.y - A.y) ** 2)

        perimeter = AB + BC + AC

        return perimeter

    # @property
    def compute_area(self):
        area = 0.5 * abs(self.point_1.x * (self.point_2.y - self.point_3.y) +
                         self.point_2.x * (self.point_3.y - self.point_1.y) +
                         self.point_3.x * (self.point_1.y - self.point_2.y))

        return area

    def change_point_or_points(self, **kwargs):

        original_point_1 = self.point_1
        original_point_2 = self.point_2
        original_point_3 = self.point_3

        for key, value in kwargs.items():
            if key[:6] == 'point_':
                self.__dict__[key] = value
        if (self.point_2.y - self.point_1.y) * (self.point_3.x - self.point_1.x) == \
                (self.point_3.y - self.point_1.y) * (self.point_2.x - self.point_1.x):
            print('Incorrect input, triangle not modified.')
            self.point_1 = original_point_1
            self.point_2 = original_point_2
            self.point_3 = original_point_3
        else:
            self.perimeter = self.compute_perimeter()
            self.area = self.compute_area()


p1 = Point(1, 2)
p2 = Point(4, 8)
# p3 = Point(2, 4)

# Triangle(point_1=p1, point_2=p2, point_3=p3)

p3 = Point(3, 5)

# Triangle(p1, p2, p3)

triangle = Triangle(point_1=p1, point_2=p2, point_3=p3)

p3 = Point(2, 4)

# triangle.change_point_or_points(p3)

triangle.change_point_or_points(point_3=p3)

p0 = Point(0, 0)
p3 = Point(0, 4)

triangle.change_point_or_points(point_3=p3, point_1=p0)

triangle.change_point_or_points(point_2=Point(4, 0))

triangle.change_point_or_points(point_3=Point(4, 0))

triangle.change_point_or_points(point_3=Point(4, 8))

print(triangle.perimeter)
print(triangle.area)

# triangle.perimeter()
# triangle.area()
