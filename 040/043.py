from itertools import permutations

def rule(p, i, m):
  return int(p[i:i+3]) % m == 0

primes = [2, 3, 5, 7, 11, 13, 17]
def rules(p):
  for i in range(7):
    if not rule(p, i + 1, primes[i]):
      return False
  return True


matches = []
for p in permutations("1234567890"):
  if rules(''.join(p)):
    matches.append(int(''.join(p)))
 
print sum(matches)

