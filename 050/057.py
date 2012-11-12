from fractions import Fraction
from math import log

def root_gen(m = None):
  count = 0
  x = 0
  while m is None or count < m:
    x = Fraction(1, 2 + x)
    yield 1 + x
    count += 1

def num_digits(n):
  return int(log(n, 10))

limit = 1000

count = 0
for f in root_gen(limit):
  n = num_digits(f.numerator)
  d = num_digits(f.denominator)
  if (n > d):
    count += 1

print count
