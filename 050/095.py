from helpers import all_factors, cached_prime

def buildChain(seed):
  s = list()
  m = seed
  while not m in s:
    if m >= 1000000:
     return [] 
    s.append(m)
    m = sum(all_factors(m)) - m
  s.append(m)
  return s

limit = 1000000
cached_prime(1000000)

m = 0
for i in range(limit):
  chain = buildChain(i)
  if len(chain) > 1 and chain[0] == chain[-1]:
    if len(chain) > m:
      m = len(chain)
      print (i, chain)
  if i % 10000 == 0:
    print i
