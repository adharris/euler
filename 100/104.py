from math import sqrt, pow, log

def fib():
  x0 = 0
  x1 = 1
  while True:
    n = x1 + x0
    x0 = x1
    x1 = n
    yield x1

def first9(n):
  return str(n)[:9]

def last9(n):
  s = str(n)
  return s[len(s)-9:]


def isPandigital(n):
  m = 123456789
  digits = 0
  if n >= m:
    while n > 0:
      digits |= 1 << (n - ((n / 10) * 10))
      n /= 10
    return digits == 1022
  return False

def last9(n):
  return n % 1000000000;

def first9(n):
  d = int(log(n, 10))
  return int(n / (10**(d-8)))

def main():
  for i,n in enumerate(fib():
    if isPandigital(last9(n)) and isPandigital(first9(n)):
      print n
      print i + 2
      break



if __name__ == '__main__':
  main()