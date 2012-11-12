from pprint import pprint

def spiral(n):
  if n % 2 == 0: return []
  sp = []
  for i in range(0, n):
    sp.append([0] * n)

  x = int(n / 2) 
  y = int(n / 2) 
  sp[x][y] = 1

  size = 2
  i = 2

  while i < n**2:
    #down
    for j in range(0, size):
      sp[y + j][x+1] = i 
      sp[y + size - 1][x - j] = i + size
      sp[y + size - j - 2][x - size + 1] = i + size * 2
      sp[y - 1][x - size + 2 + j] = i + size * 3
      i += 1
    i += size * 3
    size += 2
    x += 1
    y -= 1
  
  return sp

def sprint(s):
  pprint(map(lambda x: map(lambda y: '%02d' % y, x), s))


size = 1001
s = spiral(size)

total = 1
for i in range(size):
  if i != size/2:
    total += s[i][i]
    total += s[size-i-1][i]

print total

