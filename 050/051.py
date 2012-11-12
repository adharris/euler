from helpers import cached_prime, global_primes

limit = 1000000
family_size = 8
cached_prime(limit)
primes = global_primes()

def masks(n):
  s = str(n)
  for i in range(1,2**len(s)-2):
    cs = bin(i)[2:]
    ss = bytearray(s)
    for c in range(len(cs)):
      if cs[c] == '1':
        ss[c] = 'X'
    yield str(ss)

def find_family():
  for p in primes:
    for m in masks(p):
      family = [m.replace('X', str(i)) for i in range(10)]
      prime_family = filter(lambda x: cached_prime(int(x)), family)
      if len(prime_family) == family_size:
        print prime_family
        print m
        print p
 
find_family()
