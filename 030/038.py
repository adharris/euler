from itertools import permutations

perms = permutations("123456789")
perms = map(lambda x: ''.join(x), perms)

known_min = '918273645'
possible = filter(lambda x: x > known_min, perms)

r = range(1, 3)
for d in range(9000, 10000):
  v = ''.join(map(lambda x: str(x * d), r))
  if v in possible:
    print v
