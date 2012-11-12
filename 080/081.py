from pprint import pprint

def get_matrix(name):
  lines = open(name).read().splitlines()
  return [[int(i) for i in l.split(',')] for l in lines]

def min_none(x, y):
  if x is None and y is None: return 0
  if x is None: return y
  if y is None: return x
  return min(x, y)

def collapse(matrix, diagonal):
  for x in range(diagonal):
    y = diagonal - x - 1
    if y >= len(matrix): continue
    if x >= len(matrix[y]): continue
    if x - 1 < 0: left = None
    else: left = matrix[y][x - 1]
    if y - 1 < 0: top = None
    else: top = matrix[y - 1][x]
    matrix[y][x] += min_none(left, top)
  return matrix

def smallest_path(matrix):
  for i in range(2, len(matrix) * 2):
    matrix = collapse(matrix, i)
  return matrix[-1][-1]

matrix = get_matrix('matrix.txt')
small_matrix = [[131, 673, 234, 103, 18],
                [201, 96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524, 37, 331]]

assert smallest_path(small_matrix) == 2427
print smallest_path(matrix)
