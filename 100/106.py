from itertools import product

set4_1 = [3, 5, 6, 7]
set4_2 = [3, 5, 6, 8]

set4 = range(1, 5)
set7 = range(1, 8)

def disjointSubsets(s):
  seen_masks = set()
  for mask in product("012", repeat=len(s)):
    this_mask = ''.join(mask)
    same_mask = ''.join(['0' if a == '0' else ('2' if a == '1' else '1') for a in mask])
    if same_mask in seen_masks:
      continue
    seen_masks.add(this_mask)
    set1 = []
    set2 = []
    l = list(s)
    for i in range(len(s)):
      if mask[i] == "1":
        set1.append(l[i])
      elif mask[i] == "2":
        set2.append(l[i])
    if len(set1) > 0 and len(set2) > 0:
      yield(set1, set2)

def pairwise_compare(sets):
  gt = True
  lt = True
  s1 = sets[0]
  s2 = sets[1]
  for i in range(len(s1)):
    gt = gt and s1[i] > s2[i]
    lt = lt and s1[i] < s2[i]
  return lt or gt

def checks_needed(s):
  sets = disjointSubsets(s)
  # we dont need to check any that arent the same length, rule ii:
  sets = filter(lambda x: len(x[0]) == len(x[1]), sets)

  # we dont need to check any length = 1, because strictly increasing:
  sets = filter(lambda x: len(x[0]) > 1, sets)

  # we dont need to check ones that the max of the first is less than the min of the second:
  sets = filter(lambda x: max(x[0]) > min(x[1]), sets)

  # we dont need to check ones that the ith element of the first is less than the ith element
  # of the second for all i's
  sets = filter(lambda x: not pairwise_compare(x), sets)

  return sets

def main():
  s = range(1, 13)
  print len(checks_needed(s))

if __name__ == '__main__':
  main()