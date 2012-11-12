import math
from helpers import factor, triangle_gen

def triangle(n):
  return n * ( n + 1) / 2

def num_divisors(n):
  f =  factor(n)
  count = 0
  val = 0
  prod = 1
  for p in f:
    if p != val:
      prod *= (count + 1)
      count = 0
    val = p
    count += 1
  prod *= (count + 1)
  return prod

limit = 20000
num = 0
last_count = 0

for i in triangle_gen():
  d = num_divisors(i)
  if d > last_count:
    print "%s divisors at %s" % (d, i)
    last_count = d
