
def chain(n, change, check):
  while not check(n):
    n = change(n)
  return n

def sum_of_square_digit(n):
  total = 0
  while n > 0:
    total += (n % 10)**2
    n = n / 10
  return total

bound = 10000000
count = 0
for i in range(1, bound):
  if chain(i, sum_of_square_digit, lambda x: x == 89 or x == 1) == 89:
    count += 1
print count
