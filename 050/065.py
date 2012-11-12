from fractions import Fraction

def d(k):
  if k == 0:
    return 2
  if k % 3 == 2:
    return 2 * (k + 1)/3
  return 1

def term(n):
  f = 0
  for i in range(n, 0, -1):
    f = Fraction(1, (d(i) + f))
  return d(0) + f
    
print sum([int(x) for x in str(term(99).numerator)])
