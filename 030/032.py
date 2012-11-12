from itertools import permutations

perms = permutations('123456789')
perms = map(lambda x: ''.join(x), perms)

count = 0

match = set([])
for pan in perms:
  count += 1
  for i in range(4):
    for j in range(i + 1, i + 4):
      if int(pan[0:i+1]) * int(pan[i+1:j+1]) == int(pan[j+1:]):
        match.add(int(pan[j+1:]))
        print "%s x %s = %s (%s%%)" % (pan[0:i+1], pan[i+1:j+1], pan[j+1:], 100 * count / len(perms))
 
print match
print sum(match)
