from helpers import fibo

limit = 1000

i = 0
for f in fibo():
  i += 1
  if len(str(f)) == limit:
    print f
    print i
    break
