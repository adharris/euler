from random import randint
from fractions import gcd, Fraction
from Queue import Queue
from collections import defaultdict
from math import sqrt

def cont_fraction(S):
  a = [int(sqrt(S))]
  m = [0]
  d = [1]
  i = 0
  while True:
    i += 1
    m.append(d[i-1] * a[i-1] - m[i-1])
    d.append( (S - m[i]**2) / d[i-1] )
    a.append(int((a[0] + m[i])/d[i]))
    if i > 1 and (a[1], m[1], d[1]) == (a[i], m[i], d[i]):
      return (a[0], a[1:-1])

def cont_fraction_term(rep, n):
  f = 0
  for i in range(n, 0, -1):
    f = Fraction(1, (rep[1][(i - 1) % len(rep[1])]) + f)
  return rep[0] + f

largest_sieve = []
largest_sieve_size = 0
def is_prime(n):
  if n < largest_sieve_size:
    return n in largest_sieve

  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def prime_gen(max_size = None, max_count = None, cache = 100000, cache_increaser = lambda x: x*10):
  sieve(cache)
  index = 0
  while True:
    if index >= len(largest_sieve):
      new_cache = cache_increaser(cache)
      if new_cache is None:
        return
      print "Increasing prime_gen cache fro %s to %s" % (cache, new_cache)
      cache = new_cache
      sieve(cache)
    prime = largest_sieve[index]
    if not max_size is None and prime >= max_size:
      return
    yield prime
    index += 1
    if not max_count is None and index >= max_count:
      return

def sieve(n):
  global largest_sieve_size 
  global largest_sieve
  if n > largest_sieve_size:
    primes = do_sieve(n)
    largest_sieve = primes
    largest_sieve_size = n
    return primes
  else:
    return filter(lambda x: x < n, largest_sieve)

def do_sieve(n):
  if n == 0: return []
  if n == 1: return []
  if n == 2: return [2]
  primes = [False] * n
  primes[0] = True
  primes[1] = True
  
  p = 2 
  while p**2 < n:
    for i in range(p**2, n, p):
      primes[i] = True
    p = sieve_next_false(primes, p)

  return [i for i, x, in enumerate(primes) if not x]

def sieve_next_false(primes, n):
  while n < len(primes) - 1:
    n = n + 1
    if not primes[n]:
      return n
  return None

def get_prime_mask(primes, size):
  is_prime = [False] * (size + 1)
  for p in primes:
    is_prime[p] = True
  return is_prime

g_prime_mask = []
g_primes = []
def cached_prime(n):
  global g_primes
  global g_prime_mask
  if n > len(g_prime_mask) - 1:
    print "Building first %s primes" % n
    g_primes = sieve(n + 1)
    print "Done."
    g_prime_mask = get_prime_mask(g_primes, n + 1)
  return g_prime_mask[n]

def global_primes():
  return g_primes

def triangle(n):
  return n * (n + 1) / 2
def triangle_gen():
  i = 2
  while True:
    yield triangle(i)
    i += 1

def pentagon(n):
  return n * (3 * n - 1 ) / 2
def hexagon(n):
  return n * (2 * n - 1)

# Prime factor
def brent(n):
  if n % 2 == 0:
    return 2
  y, c, m = randint(1, n-1), randint(1, n-1), randint(1, n-1)
  g, r, q = 1, 1, 1
  while g == 1:
    x = y
    for i in range(r):
      y = ( (y * y) % n + c ) % n
    k = 0
    while k < r and g == 1:
      ys = y
      for i in range(min(m, r-k)):
        y = ( (y * y) % n + c ) % n
        q =  q * ( abs(x - y)) % n
      g = gcd(q, n)
      k = k + m
    r = r*2
  if g == n:
    while True:
      ys = ((ys * ys) % n + c) % n
      g = gcd(abs(x - ys), n)
      if g > 1:
        break
  return int(g)

def factor(n):
  if n == 1: return {}
  if n == 2: return {2:1}
  cached_prime(n)
  q = Queue()
  factors = defaultdict(int)
  q.put(n)
  while not q.empty():
    i = q.get()
    g = brent(i)
    if cached_prime(g) and g == i:
      factors[g] += 1
    else:
      q.put(g)
      if i / g != 1:
        q.put(i / g) 
  return factors

def d_factor(n):
  for p in prime_gen(max_size=n/2+1):
    if n % p == 0:
      yield p
      while n % p == 0:
        n = n / p
      if n == 1:
        break
  if is_prime(n): yield n

def all_factors(n):
  if n == 0:
    return
  if n == 1:
    yield 1
    return
  if n == 2:
    yield 1
    yield 2
    return
  factors = list(factor(n).iteritems())
  nfactors = len(factors)
  f = [0] * nfactors
  while True:
    yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
    i = 0
    while True:
      f[i] += 1
      if  f[i] <= factors[i][1]:
        break
      f[i] = 0
      i += 1
      if i >= nfactors:
        return

def totient(n):
  f = factor(n)
  prod = 1
  for p in f:
    prod *= (1 - float(1) / p)
  return int(round(prod * n))

def fibo(n = None):
  yield 1
  yield 1
  n1 = 1
  n2 = 1
  count = 2
  while True:
    n3 = n1 + n2 
    n1 = n2
    n2 = n3
    count += 1
    yield n2
    if n is not None and n <= count:
      return
    
class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned 
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)


def dump_args(func):
    "This decorator dumps out the arguments passed to a function before calling it"
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name
    
    def echo_func(*args,**kwargs):
        print fname, ":", ', '.join(
            '%s=%r' % entry
            for entry in zip(argnames,args) + kwargs.items())
        return func(*args, **kwargs)
    
    return echo_func
