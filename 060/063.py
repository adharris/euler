from math import log

def is_nth_power(i, n):
  s = int(i**(1.0/n))
  return s**n == i or (s+1)**n == i or (s-1)**n == i

count = 0
for exp in range(1,100):
  start = 10**(exp-1)
  end = 10**exp-1
  base = int(start**(1.0/exp))
  while base**exp < end + 1:
    if len(str(base**exp)) == exp:
      print ("%s**%s" % (base, exp), base**exp, len(str(base**exp)))
      count += 1
    base += 1

print count
