from helpers import memoized, dump_args, all_factors, cached_prime

@memoized
def P(n):
  if n < 0: val = 0
  elif n == 0: val = 1
  else: 
    i = 0
    s = 0
    while True:
      i += 1
      m1 = n - i * ( 3 * i - 1) / 2
      m2 = n - i * ( 3 * i + 1) / 2
      t = 1
      if i % 2 == 0: t = -1
      s += t * P(m1)
      s += t * P(m2)
      if m1 < 0 and m2 < 0: break
    val = s
  return val


def a_n(n):
  return 1

@memoized
def c_n(n):
  return sum(all_factors(n))

@memoized
def b_n(n):
  return (c_n(n) + sum([c_n(k) * b_n(n-k) for k in range(1, n)])) / n 

def first_P_div_by(n):
  cached_prime(10**6)
  i = 1
  while True:
    i += 1
    if P(i) % n == 0:
      return (i, P(i))

for i in range(1, 7):
  print first_P_div_by(10**i)
