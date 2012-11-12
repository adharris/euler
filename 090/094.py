from math import sqrt

def triangles(max_perimeter):
  i = 2
  while i * 3 - 1 <= max_perimeter:
    if i * 3 - 1 <= max_perimeter and i != 1:
      yield (i, i, i - 1)

    if i * 3 + 1 <= max_perimeter:
      yield (i, i, i + 1)

    i += 1

def area(a, b):
  return b * sqrt(4.0 * a**2 - b**2) / 4.0

p = 0
i = 0
for t in triangles(10000000):
  i += 1
  if i % 1000000 == 0:
    print i
  a = area(t[0], t[2])
  if a % 1 == 0:
    p += sum(t)
    print (t, a, p)

