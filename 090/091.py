from itertools import product
from math import sqrt

def pythag(point1, point2):
  return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

def get_points(n):
  return product(range(n+1), repeat=2)

def get_triangles(n):
  points = filter(lambda x: x != (0, 0), get_points(n))
  for point1, point2 in product(points, repeat=2):
    if point1 != point2 and is_right(point1, point2):
      yield ((0,0), point1, point2)

def get_sides(point1, point2, point3):
  side1 = pythag(point1, point2)
  side2 = pythag(point2, point3)
  side3 = pythag(point3, point1)
  return (side1, side2, side3)

def is_right(point1, point2):
  sides = sorted(get_sides((0,0), point1, point2))
  return (sides[0] + sides[1] == sides[2]) and (sqrt(sides[0]) + sqrt(sides[1]) > sqrt(sides[2]))

triangles = get_triangles(50)
print len(list(triangles)) / 2 