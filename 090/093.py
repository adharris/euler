from itertools import combinations, permutations, product

placeholders = [
  '( {0}.0 {4} ( {1}.0 {5} ( {2}.0 {6} {3}.0 ) ) )', # ( 1 + ( 2 + ( 3 + 4 ) ) )   321
  '( {0}.0 {4} ( ( {1}.0 {5} {2}.0 ) {6} {3}.0 ) )', # ( 1 + ( ( 1 + 2 ) + 4 ) )   231
  '( ( {0}.0 {4} ( {1}.0 {5} {2}.0 ) ) {6} {3}.0 )', # ( ( 1 + ( 2 + 3 ) ) + 4 )   213
  '( ( {0}.0 {4} {1}.0 ) {5} ( {2}.0 {6} {3}.0 ) )', # ( ( 1 + 2 ) + ( 3 + 4 ) )   132
  '( ( ( {0}.0 {4} {1}.0 ) {5} {2}.0 ) {6} {3}.0 )', # ( ( ( 1 + 2 ) + 3 ) + 4 )   123
]

def plus(a, b):
  return a + b

def minus(a, b):
  return a - b

def mult(a, b):
  return a * b

def div(a, b):
  return a / b

def targets(digits):
  operations = ['+', '-', '*', '/']

  for digit in permutations(digits):
    for ops in product(operations, repeat=3):
      for f in all_forms(digit, ops):
        yield f

def do_operations(digits, operations):
  digits = digits.__iter__()
  total = digits.next()
  for op in operations:
    total = op(total, digits.next())
  return total

  digit_orders = permutations(digits)
sets = combinations(range(1, 10), 4)

def all_forms(digits, ops):
  for p in placeholders:
    s = p.format(digits[0], digits[1], digits[2], digits[3], ops[0], ops[1], ops[2])
    try:
      v = eval(s)
    except:
      v = 0
    if v % 1 == 0:
      yield v

def consect(s):
  i = 0
  for d in s:
    if i == d:
      i += 1
    else:
      return i - 1


m = 0
for s in combinations(range(1, 10), 4):
  d = consect(set(targets(s)))
  if d > m:
    print (s, d)
    m = d
