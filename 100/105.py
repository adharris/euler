from itertools import product

def loadSets():
  f = open('sets.txt')
  for line in f.readlines():
    yield [int(i) for i in line.strip().split(',')]

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

def main():
  total = 0
  for s in loadSets():
    if isSpecialSet(s):
      print (sum(s), s)
      total += sum(s)
  print total


if __name__ == '__main__':
  main();