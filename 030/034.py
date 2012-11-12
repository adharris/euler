from math import factorial

def digit_map(n, callback):
  for i in str(n):
    yield callback(int(i))

def equal_factorial():
  i = 10
  while True:
    if i == sum(digit_map(i, factorial)):
      yield i
    i += 1

for i in equal_factorial():
  print i
