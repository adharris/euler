from helpers import sieve
limit = 1000

def find_longest(n):
  if n == 2: return 0
  if n == 5: return 0
  k = 1
  while True:
    if 10**k % n == 1:
      return k
    k += 1

primes = sieve(limit)
m = 0
mi = 0
for p in primes:
  l = find_longest(p)
  if l > m:
    m = l
    mi = p

print (mi, m)
