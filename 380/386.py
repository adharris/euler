from helpers import cached_prime, all_factors

limit = 10**8
cached_prime(limit + 1)

for i in range(2, limit + 1):
  list(all_factors(i))
