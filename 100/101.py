from collections import defaultdict
from numpy import matrix, linalg

class Function:
  # Polynomial functionsa are of the form a*n^b for different powers of n
  def __init__(self):
    self.coefficents = dict()

  def setCoefficent(self, power, coefficent):
    self.coefficents[power] = coefficent

  def largestPower(self):
    return max(self.coefficents.keys())

  def __call__(self, n):
    total = 0
    for key, value in self.coefficents.iteritems() :
      total += value * n**key
    return total

  def __str__(self):
    s = ""
    items = list(self.coefficents.iteritems())
    items.reverse()
    for key, value in items:
      if value == 0:
        continue
      if s != "" or value < 0:
        s += " + " if value > 0 else " - "
      if key == 0:
        s += str(abs(value))
      elif value == 1:
        s += "n^%d" % (key)
      else:
        s += "%dn^%d" % (abs(value), key)
    return s

def interpolate(x_values, y_values):
  m = []
  for i in range(len(x_values)):
    m_i = [x_values[i] ** j for j in range(len(x_values) -1, -1, -1)]
    m.append(m_i)
  A = matrix(m)
  b = matrix(y_values).T
  x = linalg.solve(A, b).tolist()
  f = Function()
  for i in range(len(x_values)):
    f.setCoefficent(i, int(round(x[len(x_values)-i-1][0])))
  return f

def findBOPS(function):
  x_values = []
  y_values = []
  for i in range(1, function.largestPower() + 1):
    x_values.append(i)
    y_values.append(function(i))
    f = interpolate(x_values, y_values)
    yield f

def findFIT(function_1, function_2):
  i = 1
  while(function_1(i) == function_2(i)):
    i = i + 1
  return i

def sumFITs(function):
  s = 0
  for bop in findBOPS(function):
    fit = findFIT(function, bop)
    s += bop(fit)
  return s


def main():
  u = Function()
  for i in range(11):
    u.setCoefficent(i, 1 if i % 2 == 0 else -1)
  print u

  cubed = Function()
  cubed.setCoefficent(3, 1)

  assert( sumFITs(cubed) == 74)

  print sumFITs(u)


if __name__ == '__main__':
  main()