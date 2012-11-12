from helpers import sieve

def poly(n, a, b):
  return n**2 + a * n + b

a_max = 1000
b_max = 1000
known_max = 81

largest_possible = poly(known_max, a_max, b_max)

primes = sieve(largest_possible)
prime_mask = [False] * largest_possible
for p in primes:
  prime_mask[p] = True

max = 0
max_a = None
max_b = None

for a in range(-a_max, a_max):
  for b in range(-b_max, b_max):
    n = 0
    while True:
      p = poly(n, a, b)
      if not prime_mask[p]:
        break
      else:
        n += 1
    if n > max:
      print "%s primes for %s, %s" % (n, a, b)
      max = n
      max_a = a
      max_b = b

print max
print max_a
print max_b
print max_a * max_b
print [poly(i, max_a, max_b) for i in range(max)]
