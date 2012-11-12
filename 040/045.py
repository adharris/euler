from helpers import triangle, pentagon, hexagon
from math import sqrt

def pent_from_tri(t):
  t = float(t)
  return (float(1) / 6) * ( 1 + sqrt( 12 * t**2 + 12 * t +1 ))

def hex_from_tri(t):
  return (t + 1) / 2

def hex_from_pent(t):
  p = float(t)
  return (float(1) / 4) * ( 1 + sqrt( 12 * t**2 - 4 * t +1 ))

for t in range(100000):
  p = pent_from_tri(t)
  h = hex_from_tri(t)
  h2 = hex_from_pent(p)
  if p % 1 == 0 and h % 1 == 0 and h2==h:
    print ((t, triangle(t)), (p, pentagon(p)), (h, hexagon(h)))
