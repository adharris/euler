def is_right_triangle(t):
  t = sorted(t)
  return t[0]**2 + t[1]**2 == t[2]**2

def tris(p):
  triangles = set([])
  for a in range(1, p - 2):
    for b in range(a, p - a-1):
      c = p - a - b
      if is_right_triangle((a,b,c)):
        triangles.add(tuple(sorted([a,b,c])))
  return triangles

max = 0
max_p = 0
for p in range(1001):
  t = len(tris(p))
  if t > max:
    max = t
    max_p = p

print max_p
