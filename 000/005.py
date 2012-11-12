primes = [1,2,2,2,2,3,3,5,7,11,13,17,19]
total = 1
for p in primes:
  total = p * total
print total

for i in range(1, 21):
  print (i, float(total) / i)
