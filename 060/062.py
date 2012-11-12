from itertools import permutations
from collections import defaultdict

def is_cube(n):
  root = int(n**(1.0/3))+1
  return root**3 == n

def perms(i):
  s = str(i**3)
  ps = filter(is_cube, (set(map(lambda x: int(''.join(x)), permutations(s)))))
  if len(ps) == 5:
    print (i, s, ps)
    max_len = len(ps)

memo = defaultdict(int)
for i in range(1, 100000):
  s = ''.join(sorted(str(i**3)))
  memo[s] += 1

for i in range(1, 100000):
  s = ''.join(sorted(str(i**3)))
  if memo[s] == 5:
    print (i, i**3, s, memo[s])
    break
