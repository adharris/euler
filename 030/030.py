power = 5
limit = 200000

def digit_powers(n, power):
  for i in str(n):
    yield int(i)**power

numbers = []
for i in range(10, limit):
  powers = sum(digit_powers(i, power))
  if powers == i:
    numbers.append(i)

print numbers
print sum(numbers)
