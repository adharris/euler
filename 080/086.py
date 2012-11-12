from math import sqrt
from helpers import memoized

def shortest_path(a, b, c):
  return min(sqrt( (a + b)**2 + c**2), sqrt( (b + c)**2 + a**2), sqrt((c + a)**2 + b**2))

def is_int(n):
  return int(n) == n

def longest_path(M):
  count = 0
  max_dist = 0
  for a in range(M, 0, -1):
    for b in range(a, 0, -1):
      for c in range(b, 0, -1):
        p = shortest_path(a, b, c)
        if is_int(p):
          return p

def integer_paths(M):
  count = 0
  max_dist = 0
  for a in range(M, 0, -1):
    for b in range(a, 0, -1):
      for c in range(b, 0, -1):
        p = shortest_path(a, b, c)
        if is_int(p):
          #print ((a, b, c), p)
          count +=1 
          if p > max_dist:
            max_dist = p
  return count

def get_triple(m, n):
  return (m**2 - n**2, 2 * m * n, m**2 + n**2)

def made_with(M, t):
  return (t[0] <= M * 2  and t[1] <= M) or (t[0] <= M and t[1] <= 2 * M)

def possible_paths(triple, M):
  count = 0
  for c in range(1, M +1):
    a = triple[0] - c
    b = triple[1]
    if a > M or b > M: continue
    if is_int(shortest_path(a, b, c)):
        count += 1
  for c in range(1, M +1):
    a = triple[0]
    b = triple[1] - c
    if a < b: continue
    if a > M or b > M: continue
    if is_int(shortest_path(a, b, c)):
      count += 1
  return count

@memoized
def P(n):
  if n < 0: val = 0
  elif n == 0: val = 1
  else: 
    i = 0
    s = 0
    while True:
      i += 1
      m1 = n - i * ( 3 * i - 1) / 2
      m2 = n - i * ( 3 * i + 1) / 2
      t = 1
      if i % 2 == 0: t = -1
      s += t * P(m1)
      s += t * P(m2)
      if m1 < 0 and m2 < 0: break
    val = s
  return val

def paths(M):
  max_dist = int(shortest_path(M, M, M))
  max_length = 3 * M + max_dist

  memo = set([])

  m = 2
  cont = True
  while cont:
    found = False
    for n in range(1, m): 
      tri = get_triple(m, n)
      k = 1
      while True:
        kt = tuple(sorted([ z * k for z in tri]))
        s = sum(kt)
        if s > max_length:
          break
        found = True
        memo.add(kt)
        k+=1
    cont = found
    m += 1
  tuples = memo
  tuples = filter(lambda x: x[2] <= max_dist, tuples)
  for t in tuples:
    #print (t, possible(t, M))
    pass
  global poss_memo
  poss_memo = set([])
  return sum(map(lambda x: possible(x, M), tuples))

poss_memo = set([])
def possible(triple, M):
  global poss_memo
  count = 0
  for i in range(1, triple[0] / 2 + 1):
    t = tuple(sorted((triple[0] - i, i, triple[1])))
    if t not in poss_memo:
      poss_memo.add(t)
      p = shortest_path(t[0], t[1], t[2])
      if is_int(p) and max(t) <= M:
        # print (triple[0] - i, i, triple[1])
        count += 1
  for i in range(1, triple[1] / 2 + 1):
    t = tuple(sorted((triple[1] - i, i, triple[0])))
    if t not in poss_memo:
      poss_memo.add(t)
      p = shortest_path(t[0], t[1], t[2])
      if is_int(p) and max(t) <= M:
        # print (triple[0] - i, i, triple[1])
        count += 1
  return count


def search_for(fn, check, low, high):
  if low == high or low + 1 == high:
    return high
  middle = low + (high - low) / 2
  val = fn(middle)
  p = check(val)
  print "high: %s, low:%s, checking %s: %s" % (high, low, middle, val)
  if not p:
    return search_for(fn, check, middle, high)
  else:
    return search_for(fn, check, low, middle)


#print search_for(integer_paths, lambda x: x > 1000) 
print search_for(paths, lambda x: x > 1000000, 1, 2000)

