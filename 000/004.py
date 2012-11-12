from math import floor, sqrt

a = 0
b = 0
c = 0

def pal6(i,j,k):
  return i + j * 10 + k * 100 + k * 1000 + j * 10000 + i * 100000 

def find_pals():
  pals = []
  for i in range(9, -1, -1):
    for j in range(9, -1, -1):
      for k in range(9, -1, -1):
        pals.append(pal6(i,j,k))
  return sorted(pals, reverse=True)

def divise_by_three_digit(x):
  for i in range(int(sqrt(x)), 100, -1):
    if x % i == 0 and x/i < 999 and x/i > 100:
      return True

  return False

print filter(divise_by_three_digit, find_pals())
