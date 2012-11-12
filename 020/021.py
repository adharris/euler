from helpers import all_factors, cached_prime, factor
from collections import defaultdict

limit = 10000
visited = defaultdict(bool)
cached_prime(limit * 10)

numbers = []

for i in range(1, limit):
  if not visited[i]:
    s = sum(all_factors(i)) - i
    if i == sum(all_factors(s)) - s:
      if i != s:
        numbers.append(i)
        numbers.append(s)
        print (i, s)
    visited[i] = True
    visited[s] = True

print sum(numbers)
