
def rectangles(x, y):
  count = 0
  for width in range(x):
    for height in range(y):
      count += (x - width) * (y - height)
  return count

def closest_to(target, threshold=.40):
  found = float('inf')
  last_found = 0
  i = 1
  while True:
    for j in range(i + 1):
      r = rectangles(i, j)
      if abs(r - target) < found:
        last_found = 0
        found = abs(r - target)
        print "%sx%s, %s rectangles, %s area" % (i, j, r, i * j)
      last_found += 1
      if last_found > target * threshold:
        return
    i += 1

closest_to(2000000)
