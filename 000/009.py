def is_triple(x):
  x = sorted(x)
  return x[0] * x[0] + x[1] * x[1] == x[2] * x[2]

def find_triple(total):
  for a in range (1, total - 1):
    for b in range (1, total - a - 1):
      c = total - a - b
      if(is_triple((a,b,c))):
        return (a, b, c)
      

triple = find_triple(1000)
print triple
print triple[0] * triple[1] * triple[2]

