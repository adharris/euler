from helpers import prime_gen, is_prime, sieve
from math import log

family_size = 4

def int_concat(n1, n2):
  return n1 * 10**(int(log(n2, 10)) + 1) + n2

def int_split(n, d):
  left = n / 10**d
  right = n % 10**d
  if int_concat(left, right) == n:
    return (left, right)

def is_family(f):
  for i in range(len(f)):
    for j in range(i + 1, len(f)):
      left = int_concat(f[i], f[j])
      right = int_concat(f[j], f[i])
      if not (is_prime(left) and is_prime(right)):
        return False
  return True

sieve(100000000)
max_prime = 10000
fam_size = 3

primes = list(prime_gen(max_size = max_prime))
def fams():
  for i in range(1, len(primes)):
    for j in range(i+1, len(primes)):
      if not is_family((primes[i], primes[j])):
        continue
      print (primes[i], primes[j])
      for k in range(j+1, len(primes)):
        if not is_family((primes[i], primes[j], primes[k])):
          continue
        for l in range(k + 1, len(primes)):
          if not is_family((primes[i], primes[j], primes[k], primes[l])) or k > l:
            continue
          for m in range(l + 1, len(primes)):
            if not is_family((primes[i], primes[j], primes[k], primes[l], primes[m])):
              continue
            return (primes[i], primes[j], primes[k], primes[l], primes[m])

f =  fams()
print f
print sum(f)
