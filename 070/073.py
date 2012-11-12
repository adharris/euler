from fractions import gcd

lower_bound = float(1) / 3
upper_bound = float(1) / 2

limit = 12000

count = 0
for d in range(1, limit + 1):
  start = lower_bound * d
  end = upper_bound * d
  for n in range(int(start)+1, int(end) + 1 ):
    if gcd(n, d) == 1 and float(n) / d != upper_bound :
      count += 1

print count

