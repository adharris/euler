from math import factorial

def C(n, r):
  return factorial(n) / ( factorial(r) * factorial(n-r))

limit = 100

count = 0
for n in range(1, limit + 1):
  for r in range(1, n + 1):
    if C(n, r) > 1000000:
      count += 1

print count
