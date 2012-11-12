import re

numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
def parse_numeral(numeral):
  i = 0
  total = 0
  while i < len(numeral):
    this_val = numeral_values[numeral[i]]
    if  i + 1 < len(numeral):
      next_val = numeral_values[numeral[i + 1]]
      if this_val < next_val:
        total += (next_val - this_val)
        i += 2
      else:
        total += this_val
        i += 1
    else:
      total += this_val
      i += 1
  return total

def to_numeral(n):
  chars = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
  s = ""
  for k,v in sorted(chars.items(), reverse = True):
    while n >= k:
      s += v
      n -= k

  return s


numerals = open('roman.txt').read().splitlines()
saved = 0
for numeral in numerals:
  value = parse_numeral(numeral)
  new = to_numeral(value)
  saved += (len(numeral) - len(new))
  print new
print saved
