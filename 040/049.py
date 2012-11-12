from helpers import sieve

def is_permutation(nums):
  c = ''.join(sorted(str(nums[0])))
  for i in nums[1:]:
    if ''.join(sorted(str(i))) != c:
      return False
  return True

primes = sieve(10000)
prime_mask = [False] * 10001
for p in primes:
  prime_mask[p] = True


for i in range(len(primes) - 2):
  j = 1
  if primes[i] < 1000:
    continue
  while primes[i] + j * 2 < 10000:
    p1 = primes[i]
    p2 = primes[i] + j
    p3 = primes[i] + j*2
    j += 1
    
    if p2 - p1 == p3 - p2 and prime_mask[p2] and prime_mask[p3]:
      if is_permutation((p1, p2, p3)):
        print (p1, p2, p3)
      
