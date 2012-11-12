def not_div_by(y):
  return lambda x: x % y != 0

def first_false(primes):
  for i in range(0, len(primes)):
    if not primes[i]:
      return i

limit = 2000000
primes = []
memo = [False] * limit
memo[0] = True
memo[1] = True

c = True
while(c):
  p = first_false(memo)
  memo[p] = True
  primes.append(p)
  if p * p > limit:
    break
  else:
    for i in range(p * p, limit, p):
      memo[i] = True

for i in range(primes[-1], len(memo)): 
  if not memo[i]:
    primes.append(i)

print sum(primes)

