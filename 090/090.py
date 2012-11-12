from itertools import combinations, product

def is_in(cube, n):
  return (n in cube) or (n == 6 and 9 in cube) or (n == 9 and 6 in cube)

def can_display(cube1, cube2, n):
  n1 = n / 10
  n2 = n % 10
  return (is_in(cube1, n1) and is_in(cube2, n2)) or (is_in(cube1, n2) and is_in(cube2, n1))

def can_display_all(cube1, cube2, ns):
  for n in ns:
    if not can_display(cube1, cube2, n):
      return False
  return True

def cubes_that_display(values):
  cubes = product(combinations(range(10), 6), repeat=2)
  for cube1, cube2 in cubes:
    if cube1 != cube2:
      if can_display_all(cube1, cube2, values):
        yield tuple(sorted((cube1, cube2)))


powers = [x**2 for x in range(1, 10)]
cubes = cubes_that_display(powers).next()
cube1 = cubes[0]
cube2 = cubes[1]
print can_display(cube1, cube2, 81)
print cube1
print cube2
print len(set(cubes_that_display(powers)))
