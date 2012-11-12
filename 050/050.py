from helpers import cached_prime, global_primes

limit = 1000000
cached_prime(limit)
primes = global_primes()

max_length = 0
data = None
for i in range(len(primes)):
  length = 1
  while True:
    if i+length > len(primes): break
    s = sum(primes[i:i+length])
    if s > limit:
      break
    if cached_prime(s):
      if max_length < length:
        print "Found length %s %s (%s%%)" % (length, s, 100 * i / len(primes))
        max_length = length
    length += 1

    
