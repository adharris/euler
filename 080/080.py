from decimal import getcontext, Decimal
from math import sqrt

def get_decimal(n):
  p = str(n).split('.')
  if len(p) > 1:
    return int(p[1][:100])
  return 0

def digital_sum(n):
  s = 0
  while n > 0:
    s += n % 10
    n /= 10
  return s

def root_digits(n):
  if int(sqrt(n))**2 == n: return 0
  return int(Decimal(n).sqrt() * 10**99)

getcontext().prec = 120
print digital_sum(root_digits(4))
print sum([digital_sum(root_digits(i)) for i in range(1, 100)])
