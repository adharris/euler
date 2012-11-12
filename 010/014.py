import operator
limit = 1000000

memo = {}
def collatz(n):
  if n == 1:
    return 1
  if not n in memo:
    if n % 2 == 0:
      b = n / 2
    else:
      b = 3 * n + 1
    c = collatz(b) + 1
    memo[n] = c
  return memo[n]

for i in range(1,limit):
  print (i, collatz(i))

    
m =  max(memo, key=lambda x: memo[x] if x < limit else 0)
print (m, memo[m])
