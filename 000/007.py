def not_div_by(y):
  return lambda x: x % y != 0

target = 10001
batch_size = 10000
primes = [2]

while(len(primes) < target):
  candidates = range(primes[-1], primes[-1]+batch_size)
  print "%s starting from prime %s: %s" % (batch_size, len(primes), primes[-1])
  for prime in primes:
    candidates = filter(not_div_by(prime), candidates)
  while(len(candidates) > 0):
    next_prime = candidates[0] 
    primes.append(next_prime)
    candidates = filter(not_div_by(next_prime), candidates)

print (len(primes), primes[-1])
print (target, primes[target -1])
