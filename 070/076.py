from collections import deque

def collapse(start, n, list):
  return list[:start] + [sum(list[start:start+n])] + list[start+n:]

def first_1(list):
  for i in range(len(list)):
    if list[i] == 1:
      return i

def collapse_first(n, list):
  first = first_1(list)
  return collapse(first, n, list)

def collapse_all(list):
  first = first_1(list)
  if first == 0 or first is None:
    return
  max_n = list[first - 1]
  if len(list[first:]) == 1:
    return
  for n in range(2, min(max_n, len(list) - first) + 1):
    yield collapse_first(n, list)

def get_first(a):
  for first_n in range(2, len(a)):
    yield collapse_first(first_n, a)

def count_combos(max_length):
  a = [1] * max_length
  q = deque(get_first(a));

  count = 1
  last = 0
  while len(q) > 0:
    l = q.popleft()
    if l[0] > last:
      print l[0]
      last = l[0]
    count += 1
    for n in collapse_all(l):
      q.appendleft(n)
  return count

memo_P = {}
def P(n):
  if n in memo_P: return memo_P[n]
  if n < 0: val = 0
  elif n == 0: val = 1
  else: val = sum([ (-1)**(k+1) * ( P(n - ( 3*k**2 - k) / 2) + P(n - ( 3*k**2 + k) / 2)) for k in range(1, n+1)])
  global memo_P
  memo_P[n] = val
  return val

for n in range(1, 101):
  print (n, P(n)-1)
