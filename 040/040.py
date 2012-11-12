def numbers(max, base):
  num = 0
  index = 1
  exp = 0
  while index <= max:
    num += 1
    for s in str(num):
      if base**exp == index:
        yield int(s)
        exp += 1
      index += 1
    
limit = 1000000
base = 10

mul = 1
for i in numbers(limit, base):
  print i
  mul *= i

print mul
