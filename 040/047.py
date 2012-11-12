from helpers import factor, cached_prime

limit = 1000000
cached_prime(limit)

c0 = len(factor(6))
c1 = len(factor(7))
c2 = len(factor(8))
c3 = len(factor(9))
for i in range(10, limit):
  c0 = c1
  c1 = c2
  c2 = c3
  c3 = len(factor(i))
  if c0 == 4 and c1 ==4 and c3 == 4 and c2 == 4:
    print i-3
