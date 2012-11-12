from math import sqrt, floor
from collections import deque
x = 600851475143

def get_largest_factor(x):
  i = floor(sqrt(x))
  while i > 0:
    if x % i == 0:
      return i
    i = i - 1

factors = deque([x])
prime_factors = []
i = 0
while(i < len(factors)):
  x = factors.popleft()
  large = get_largest_factor(x)
  if large == 1:
    prime_factors.append(x)
  else:
    factors.append(x / large)
    factors.append( large )

print prime_factors
