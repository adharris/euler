size_a = 100
size_b = 100

found = set()

for a in range(2, size_a + 1):
  for b in range(2, size_b + 1):
    found.add(a**b)

print len(found)

