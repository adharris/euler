from math import factorial

def digit_fn(n, fn):
  while n >= 10:
    yield fn(n % 10)
    n /= 10
  yield fn(n)

def chain(n):
  last = n
  yield last
  while True:
    next = sum(digit_fn(last, factorial))
    if next == last:
      return
    yield next
    if next == 169 or next == 363601 or next == 1454:
      next = sum(digit_fn(next, factorial))
      yield next
      next = sum(digit_fn(next, factorial))
      yield next
      return
    if next == 871 or next == 45361:
      next = sum(digit_fn(next, factorial))
      yield next
      return
    if next == 872 or next == 45362:
      next = sum(digit_fn(next, factorial))
      yield next
      return
    last = next

limit = 10**6
count = 0
for n in range(limit):
  l = len(list(chain(n)))
  if l == 60:
    print n
    count += 1

print count
