from itertools import permutations

def is_magic(l):
  if len(l) % 3 != 0:
    return False
  size = len(l) / 3
  max = size * 3

  outer = []
  for i in range(size):
    outer.append(l[i*3])
  if l[0] != min(outer):
    return False

  for i in range(1, size - 1):
    if l[3 * i -1] != l[3 * i + 1]:
      return false
  
  s = sum(l[:3])
  for i in range(1, size):
    if sum(l[3*i:3*i+3]) != s:
      return False

  return True

m  = [4,2,3,5,3,1,6,1,2]
print is_magic(m)

for p in permutations(range(1, 11)):
  m = [p[0], p[5], p[6], p[1], p[6], p[7], p[2], p[7], p[8], p[3], p[8], p[9], p[4], p[9], p[5]]
  if is_magic(m):
    s = ''.join(map(lambda x: str(x), m))
    if len(s) == 16:
      print s
  
