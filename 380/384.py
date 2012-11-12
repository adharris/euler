from collections import defaultdict
import math

def a(n):
  x = n & ( n << 1)
  return set_bits(x)

def a_r(n):
  if n <= 1: return 0
  else:
    po = int(math.log(n,2))
    a = 2**po
    return a_r(n - a) + int((n - a) / (po - 1))


def set_bits(n):
  n = n - ((n >> 1) & 0x55555555)
  n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
  return (((n + (n >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24

def b(n):
  return pow(-1, a(n))

s_memo = [1]
def s(n):
  if(n >= len(s_memo)):
    for i in range(len(s_memo), n+1):
      s_memo.append(s_memo[i-1] + b(i))
  return s_memo[n]

g_memo = defaultdict(list)
g_last_index = 0
def g(t,c):
  global g_last_index
  while c > len(g_memo[t]):
    value = s(g_last_index)
    g_memo[value].append(g_last_index)
    g_last_index = g_last_index + 1
    if(g_last_index % 100000 == 0):
      print (g_last_index, t,len(g_memo[t]))

  return g_memo[t][c-1]

def print_g_memo():
  for key in g_memo:
    if(len(g_memo[key]) == key): 
      print '%s: %s' % (key, sum(g_memo[key]))

fib_memo = [1, 1]
def F(t):
  if t >= len(fib_memo):
    for i in range(len(fib_memo), t+1):
      fib_memo.append(fib_memo[i-2] + fib_memo[i-1])
  return fib_memo[t]

def GF(t):
  return g(F(t), F(t-1))

for i in range(0, ):
  print (i, a(i), b(i), s(i))

g(20,20)
print_g_memo()

print [a(i) for i in range(0, 32)]
print [a_r(i) for i in range(0, 32)]
