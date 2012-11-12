limit = 100

def sum_digits(n):
  return sum(map(lambda x: int(x), str(n)))

m= 0
for i in range(limit):
  for j in range(limit):
    m = max(m, sum_digits(i**j))

print m
