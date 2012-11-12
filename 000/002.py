
total = 0
one = 0
two = 1

while (one < 4000000):
  if one % 2 == 0:
    total += one
  three = one + two
  one = two
  two = three

print total
