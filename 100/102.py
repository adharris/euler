import numpy as np

class Point:
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)
  def __str__(self):
    return "(%d, %d)" % (self.x, self.y)

  def cross(self, point):
    return np.cross([self.x, self.y], [point.x, point.y])

  def sub(self, point):
    return Point(self.x - point.x, self.y - point.y)

  def sameSideAs(self, point, line):
    cp1 = int(line.point2.sub(line.point1).cross(self.sub(line.point1)))
    cp2 = int(line.point2.sub(line.point1).cross(point.sub(line.point1)))
    return cp1 * cp2 >= 0

class Line:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def __str__(self):
    return "Line: %s to %s" % (self.point1, point2)

class Triangle:
  def __init__(self, points):
    self.a = Point(points[0], points[1])
    self.b = Point(points[2], points[3])
    self.c = Point(points[4], points[5])
  def __str__(self):
    return "A:%s B:%s C:%s" %(self.a, self.b, self.c)
  def containsPoint(self, point):
    line_a = Line(self.b, self.c)
    line_b = Line(self.c, self.a)
    line_c = Line(self.a, self.b)
    return point.sameSideAs(self.a, line_a) and point.sameSideAs(self.b, line_b) and point.sameSideAs(self.c, line_c)

def loadTriangles():
  f = open('triangles.txt')
  for line in f.readlines():
    points = line.strip().split(',')
    yield Triangle(points)

def main():
  triangles = loadTriangles();
  origin = Point(0,0)
  count = 0
  for t in triangles:
    if t.containsPoint(origin):
      count = count + 1
  print count



if __name__ == '__main__':
  main()