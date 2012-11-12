from fractions import gcd

limit = 10**6

target = float(3) / 7

found = 1

for d in range(limit + 1, 2, -1):
  best_n = target * d
  for n in range(int(best_n)+1, 1, -1):
    if gcd(n, d) == 1:
      f = target - float(n) / d
      if f > 0 and f < found:
        print (n, d, f)
        found = f
