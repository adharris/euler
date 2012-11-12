from helpers import all_factors, cached_prime

limit = 28124

cached_prime(limit)

def abundent(n):
  for i in range(n):
    s = sum(all_factors(i)) - i
    if i < s:
      yield i

abundent = list(abundent(limit))
sums = [False] * limit

for i in range(len(abundent)):
  for j in range(i, len(abundent) - i):
    k = abundent[i] + abundent[j]
    if k < limit:
      sums[k] = True

total = 0
for i in range(len(sums)):
  if not sums[i]:
    total += i

print "Total: %s" % total
