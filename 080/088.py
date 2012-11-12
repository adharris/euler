
def n_divisors(N, n):
  if n == 2:
    for i in range(2, N / 2 + 1):
      if N % i == 0:
        yield (N / i, i)
  else:
    for i in range(2, N / 2 + 1):
      if N % i == 0:
        for d in n_divisors(N / i, n - 1):
          yield tuple(sorted((i, ) + d))

def possible_divisors(N):
  i = 2
  while True:
    d = set(n_divisors(N, i))
    if len(d) == 0:
      break
    for dv in d:
      yield dv
    i += 1

def size_of_product_sums(N):
  d = sorted(possible_divisors(N), key = lambda x: len(x))
  for products in d:
    number_of_ones = N - sum(products)
    yield number_of_ones + len(products)

def sum_of_minimal(max):
  mins = [None] * (max + 1)
  n = 4
  while mins[max] is None:
    for d in size_of_product_sums(n):
      if d < len(mins) and mins[d] is None:
        mins[d] = n
    n += 1
  return sum(set(filter(lambda x: not x is None, mins)))

print sum_of_minimal(12002)
