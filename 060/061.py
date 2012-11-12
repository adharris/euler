def tri(n):
  return n * (n + 1) / 2
def sq(n):
  return n**2
def pent(n):
  return n  * (3 * n - 1) / 2
def hex(n):
  return n * ( 2 * n - 1)
def hept(n):
  return n * ( 5 * n - 3) / 2
def oct(n):
  return n * ( 3 * n - 2 )

def adj(n1, n2):
  return n1 % 100 == n2 / 100

def fn_range(start, stop, fn):
  i = 0
  while fn(i) < start:
    i += 1
  while True:
    f = fn(i)
    i += 1
    if f > stop:
      return
    yield f

def cycle_fn(cycle, functions):
  if len(functions) == 0 and adj(cycle[-1], cycle[0]):
    yield cycle
    return

  for i in range(len(functions)):
    for f in fn_range(1000, 9999, functions[i]):
      if len(cycle) == 0 or adj(cycle[-1], f):
        for c in cycle_fn(cycle + (f,), functions[:i] + functions[i+1:]):
          yield c


for t in fn_range(1000, 9999, tri):
  cycle = list(cycle_fn((t,), [sq, pent, hex, hept, oct]))
  if len(cycle) > 0:
    print (cycle, map(lambda x: sum(x), cycle))
