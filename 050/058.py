from helpers import cached_prime, is_prime

def get_prime_count(s, n):
  size = len(s)
  i = (n - 1) / 2 - 1
  c = int(size / 2)
  ul = s[c-1-i][c-1-i]
  bl = s[c+1+i][c-1-i]
  br = s[c+1+i][c+1+i]
  count += len(filter(cached_prime, (ul, bl, br)))
  return count

def get_diag_count(n):
  return 2 * (n - 1) + 1

def corners(m = None):
  i = 1
  while m is None or i < m:
    size = 2*i + 1
    c1 = size**2
    c2 = c1 - (size - 1)
    c3 = c1 - 2 * (size - 1)
    c4 = c1 - 3 * (size - 1)
    yield(size, c2, c3, c4)
    i += 1



size = 1000000
cached_prime(size)

total = 1
primes = 0
for c in corners():
  total += 4
  primes += len(filter(is_prime, c[1:]))
  if ((primes * 1000 / total) / 10.0) < 10:
    print c[0]
    break

