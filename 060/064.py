from math import sqrt

def cont_fraction(S):
  a = [int(sqrt(S))]
  m = [0]
  d = [1]
  i = 0
  while True:
    i += 1
    m.append(d[i-1] * a[i-1] - m[i-1])
    d.append( (S - m[i]**2) / d[i-1] )
    a.append(int((a[0] + m[i])/d[i]))
    if i > 1 and (a[1], m[1], d[1]) == (a[i], m[i], d[i]):
      return (a[0], a[1:-1])

count = 0
for i in range(1, 10001):
  if int(sqrt(i))**2 != i:
    if len(cont_fraction(i)[1]) % 2 == 1:
      count += 1

print count
