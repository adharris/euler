from itertools import product, combinations, chain
from math import ceil

def disjointSubsets(s):
  for mask in product("012", repeat=len(s)):
    set1 = set()
    set2 = set()
    l = list(s)
    for i in range(len(s)):
      if mask[i] == "1":
        set1.add(l[i])
      elif mask[i] == "2":
        set2.add(l[i])
    if len(set1) > 0 and len(set2) > 0:
      yield(set1, set2)

def isSpecialPair(set1, set2):
  if sum(set1) == sum(set2):
    return False
  if len(set1) > len(set2):
    return sum(set1) > sum(set2)
  elif len(set2) > len(set1):
    return sum(set2) > sum(set1)
  return True

def isSpecialSet(s):
  for subsets in disjointSubsets(s):
    if not isSpecialPair(subsets[0], subsets[1]):
      return False
  return True

def reduceToOptimum(s):
  length = len(s)
  total = sum(s)
  start = min(s)

  margin = 3;

  found = []

  masks = product(range(-1 * margin, margin + 1), repeat=len(s))
  for i, mask in enumerate(masks):
    applied = apply_mask(s, mask)
    if isSpecialSet(applied):
      found.append(applied)
      print applied
    if i % 1000 == 0:
      print i

  m = 9999999999
  for f in found:
    if sum(f) < m:
      print (f, sum(f))
      m = sum(f)

def apply_mask(s, mask):
  s = list(s)
  return [s[i] + mask[i] for i in range(len(s))]


def parts(n, length, smallest, largest=None):
  for p in parts_recur(n, length, smallest, n):
    if not largest is None and p[0] > largest:
      break
    yield p

def parts_recur(n, max_length, min_size, max_size):
  if n == 0:
    yield []
  elif min_size > max_size:
    yield []
  elif max_length == 1:
    yield [max_size]
  else:
    for x in range(min_size, max_size + 1):
      for p in parts_recur(n - x, max_length - 1, x + 1, max_size - x):
        p0 = list(chain([x], p))
        if len(p0) == max_length:
          yield p0

def findNext(s):
  l = sorted(list(s))
  middle = l[int(len(s) / 2)]
  next = set([middle])
  for i in range(len(l)):
    next.add(int(l[i]+ middle))
  return reduceToOptimum(sorted(next))


def main():
  s = {11, 18, 19, 20, 22, 25}
  s1 = {6, 9, 11, 12, 13}
  s0 = findNext(s)
  print s0
  print (s0, isSpecialSet(s))




if __name__ == '__main__':
  main()