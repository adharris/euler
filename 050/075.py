from math import sqrt
from helpers import d_factor

def get_b(a, p):
  return float(p) * (2 * a - p ) / ( 2 * ( a - p ) )

def get_triangles(L):
  max_side = int( sqrt( ( sqrt(2) * L - L )**2 / 2 ) )
  triangles = []
  for a in range(1, max_side + 1):
    b = get_b(a, L)
    if b % 1 == 0:
      c = L - a - b
      triangles.append((a, int(b), int(c)))
  return triangles

def get_triple(m, n):
  return (m**2 - n**2, 2 * m * n, m**2 + n**2)

max_length = 1500000
memo = [set([]) for i in range(max_length+1)] 

m = 2
cont = True
while cont:
  found = False
  for n in range(1, m): 
    tri = get_triple(m, n)
    k = 1
    while True:
      kt = tuple(sorted([ z * k for z in tri]))
      s = sum(kt)
      if s > max_length:
        break
      found = True
      memo[s].add(kt)
      k+=1
  cont = found
  m += 1

print len(filter(lambda x: len(x) == 1, memo))
