from itertools import islice, repeat, chain, combinations
from pprint import pprint
from copy import deepcopy
from collections import defaultdict


def load_grids():
  i = iter(map(lambda x: x.strip(), open('sudoku.txt')))
  grid = list(islice(i, 10))
  while grid:
    yield grid
    grid = list(islice(i, 10))

def prepare_grid(raw):
  for i in range(1, 10):
    yield [set([int(x)]) if int(x) != 0 else set(range(1,10)) for x in raw[i]]

def prepare_grids():
  for grid in load_grids():
    yield [row for row in prepare_grid(grid)]


def print_board(grid):
  print ' -------------------------------------------------'
  for i,row in enumerate(grid):
    if i % 3 == 0 and i != 0:
      print ' |---------------+---------------+---------------|'
    print_row(row)
  print ' -------------------------------------------------'

def print_row(row):
  for a,i in enumerate(range(3)):
    s = ""
    for b,j in enumerate(row):
      s += ' | ' if b % 3 == 0 else '  '
      for k in range(3):
        if len(j) == 1 and i == 1 and k == 1:
          s += str(list(j)[0])
        elif len(j) > 1:
          m = i * 3 + k + 1
          s += str(m) if m in j else ' '
        else:
          s += ' '
    s += ' |'
    print s

def unsolved_cells(grid):
  return sum([sum(map(lambda x: 1 if len(x) != 1 else 0, row)) for row in grid])

def first_three(grid):
  first_row = list(get_row(grid, 0, -1))
  print first_row
  return int(''.join(map(lambda x: str(sum(x)), first_row[:3])))


def rows(grid):
  for i in range(9):
    yield grid[i]

def get_row(grid, row, col):
  for i,s in enumerate(grid[row]):
    if i != col:
      yield s

def get_col(grid, row, col):
  for i in range(9):
    if i != row:
      yield grid[i][col]

def get_sub(grid, row, col):
  a = row - row % 3
  b = col - col % 3
  for i in range(3):
    for j in range(3):
      if a + i != row or b + j != col:
        yield grid[a + i][b + j]


def naked_singles(grid):
  for i in range(9):
    for j in range(9):
      if len(grid[i][j]) > 1:
        for s in chain(get_row(grid, i, j), get_col(grid, i, j), get_sub(grid, i, j)):
          if len(s) == 1:
            v = list(s)[0]
            if v in grid[i][j]:
              grid[i][j].remove(v)

def hidden_singles(grid):
  for i in range(9):
    for j in range(9):
      if len(grid[i][j]) > 1:
        for fn in [get_row, get_col, get_sub]:
          candidiates =  grid[i][j].copy()
          for exclude in fn(grid, i, j):
            candidiates -= exclude
          if len(candidiates) == 1:
            grid[i][j] = candidiates

def cleanup(grid):
  for i in range(9):
    for j in range(9):
      if len(grid[i][j]) == 1:
        v = list(grid[i][j])[0]
        t = i == 6 and j == 8
        if t:
          print v
        for k in range(9):
          if k != j and v in grid[i][k]:
            grid[i][k].remove(v)
        for k in range(9):
          if i != k and v in grid[k][j]:
            grid[k][j].remove(v)

def naked_pairs(grid):
  for i in range(9):
    for j1, j2 in combinations(range(9), 2):
      if len(grid[i][j1]) == 2 and grid[i][j1] == grid[i][j2]:
        for j0 in set(range(9)) - set([j1, j2]):
          grid[i][j0] -= grid[i][j1]
  pass

def hidden_pairs(grid):
  # rows
  for i in range(9):
    for v1, v2 in combinations(range(1, 10), 2):
      v = set([v1, v2])
      j_list = list()
      for j in range(9):
        if len(v.intersection(grid[i][j])) == 2:
          j_list.append(j)
        if len(v.intersection(grid[i][j])) == 1:
          j_list = list();
          break
      if len(j_list) == 2:
        for j in j_list:
          grid[i][j] = v.copy();

  for j in range(9):
    for v1, v2 in combinations(range(1, 10), 2):
      v = set([v1, v2])
      i_list = list()
      for i in range(9):
        if len(v.intersection(grid[i][j])) == 2:
          i_list.append(i)
        if len(v.intersection(grid[i][j])) == 1:
          i_list = list()
          break
      if len(i_list) == 2:
        for i in i_list:
          grid[i][j] = v.copy()

  #boxes
  for b in range(9):
    for v1, v2 in combinations(range(1, 10), 2):
      v = set([v1, v2])
      a_list = list()
      for a in range(9):
        i = (b / 3) * 3 + a / 3
        j = (b % 3) * 3 + a % 3
        if len(v.intersection(grid[i][j])) == 2:
          a_list.append(a)
        if len(v.intersection(grid[i][j])) == 1:
          a_list = list();
          break
      if len(a_list) == 2:
        i1 = (b / 3) * 3 + a_list[0] / 3
        j1 = (b % 3) * 3 + a_list[0] % 3
        i2 = (b / 3) * 3 + a_list[1] / 3
        j2 = (b % 3) * 3 + a_list[1] % 3
        grid[i1][j1] = v.copy();
        grid[i2][j2] = v.copy();
  naked_pairs(grid)

def get_a(i, j):
  return (i % 3) * 3 + (j % 3)
def get_b(i, j):
  return (i / 3) * 3 + (j / 3)
def get_i(a, b):
  return (b / 3) * 3 + a / 3
def get_j(a, b):
  return (b % 3) * 3 + a % 3


def pointing_pairs(grid):
  # A Pair or Triple in a box - if they are aligned on a row, n can be removed from the rest of the row.
  # A Pair or Triple in a box - if they are aligned on a column, n can be removed from the rest of the column.
  # A Pair or Triple on a row - if they are all in the same box, n can be removed from the rest of the box.
  # A Pair or Triple on a column - if they are all in the same box, n can be removed from the rest of the box.

  for b in range(9):
    for v in range(1, 10):
      cells_with_v = filter(lambda x: v in grid[x[0]][x[1]] and len(grid[x[0]][x[1]]) > 1, [(get_i(a, b), get_j(a, b)) for a in range(9)])
      same_row = True
      same_col = True
      if len(cells_with_v) > 0:
        row = cells_with_v[0][0]
        col = cells_with_v[0][1]
        for cell in cells_with_v:
          if row != cell[0]:
            same_row = False
          if col != cell[1]:
            same_col = False
        if same_row:
          for j in range(9):
            if get_b(row, j) != b and v in grid[row][j]:
              grid[row][j].remove(v)
        if same_col:
          for i in range(9):
            if get_b(i, col) != b and v in grid[i][col]:
              grid[i][col].remove(v)

  for i in range(9):
    for v in range(1, 10):
      cells_with_v = filter(lambda x: v in grid[x[0]][x[1]] and len(grid[x[0]][x[1]]) > 1, [(i, j) for j in range(9)])
      if len(cells_with_v) > 0:
        same_box = True
        box = get_b(cells_with_v[0][0], cells_with_v[0][1])
        for cell in cells_with_v:
          if box != get_b(cell[0], cell[1]):
            same_box = False
        if same_box:
          for a in range(9):
            if get_i(a, box) != i and v in grid[get_i(a, box)][get_j(a, box)]:
              grid[get_i(a, box)][get_j(a, box)].remove(v)

  for j in range(9):
    for v in range(1, 10):
      cells_with_v = filter(lambda x: v in grid[x[0]][x[1]] and len(grid[x[0]][x[1]]) > 1, [(i, j) for i in range(9)])
      if len(cells_with_v) > 0:
        same_box = True
        box = get_b(cells_with_v[0][0], cells_with_v[0][1])
        for cell in cells_with_v:
          if box != get_b(cell[0], cell[1]):
            same_box = False
        if same_box:
          for a in range(9):
            if get_j(a, box) != j and v in grid[get_i(a, box)][get_j(a, box)]:
              grid[get_i(a, box)][get_j(a, box)].remove(v)


def x_wing(grid):
  # by rows
  for i in range(9):
    for v in range(1, 10):
      v_cells = filter(lambda x: v in grid[x[0]][x[1]] and len(grid[x[0]][x[1]]) > 1, [(i, j) for j in range(9)])
      if len(v_cells) == 2:
        cell1 = v_cells[0]
        cell2 = v_cells[1]
        found = -1
        for i2 in range(i + 1, 9):
          v_cells_2 = filter(lambda x: v in grid[x[0]][x[1]] and len(grid[x[0]][x[1]]) > 1, [(i2, j) for j in range(9)])
          if len(v_cells_2) == 2 and (i2, cell1[1]) in v_cells_2 and (i2, cell2[1]) in v_cells_2:
            found = i2
            break
        if found >= 0:
          for i0 in set(range(9)) - set([i, i2]):
            if v in grid[i0][cell1[1]] and len(grid[i0][cell1[1]]) > 1:
              grid[i0][cell1[1]].remove(v)
            if v in grid[i0][cell2[1]] and len(grid[i0][cell2[1]]) > 1:
              grid[i0][cell2[1]].remove(v)


def do_until(grid, f):
  i = 0
  copy_grid = deepcopy(grid)
  f(grid)
  while grid != copy_grid:
    i += 1
    copy_grid = deepcopy(grid)
    f(grid)
  return i

def solve(grid, fn):
  i = 0
  while unsolved_cells(grid) > 0 and i < len(fn):
    c = do_until(grid, fn[i])
    if c == 0:
      i += 1
    else:
      i = 0

fn = [naked_singles, hidden_singles, naked_pairs, hidden_pairs, pointing_pairs, x_wing]
fns = defaultdict(lambda: fn)
fns[48] = [naked_singles, hidden_singles, naked_pairs, hidden_pairs, x_wing]

grids = list(prepare_grids())
total = 0
for i, grid in enumerate(grids):
  solve(grid, fns[i + 1])
  if unsolved_cells(grid) > 0:
    hidden_singles(grid)
    print "Grid %s" % (i + 1)
    print_board(grid)
    break
  else:
    print first_three(grid)
    print_board(grid)
    total += first_three(grid)
print total



