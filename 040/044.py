from math import sqrt

def pent_gen(start, end):
  for i in range(start, end):
    yield i * (3 * i - 1) / 2

def pent_inv(p):
  return (float(1) / 6) * (sqrt(24 * p + 1) + 1)

def is_pent(p):
  return pent_inv(p) % 1 == 0

limit = 10000
for p1 in pent_gen(1, limit):
  for p2 in pent_gen(int(pent_inv(p1)), limit):
    S = p1 + p2
    D = abs(p1 - p2)
    if is_pent(S) and is_pent(D):
      print (p1, p2, abs(p1 - p2))
