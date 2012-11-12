from math import sqrt
from helpers import cont_fraction, cont_fraction_term

def get_x(y, D):
  return sqrt(1 + D * y**2)

def is_solution(x, y, D):
  val = x**2 - (D * y**2)
  return val == 1

def find_min_x(D):
  f = cont_fraction(D)
  i = 0
  while True:
    t = cont_fraction_term(f, i)
    if is_solution(t.numerator, t.denominator, D):
      return t
    i += 1
  
m_x = 0
for D in range(1, 1001):
  if int(sqrt(D))**2 == D:
    continue
  t = find_min_x(D)
  if t.numerator > m_x:
    m_x = t.numerator
    print (D, t)


