def roll_up(triangle):
  last_row = triangle[-1]
  row = triangle[-2]
  new_row = []
  for i in range(len(row)):
    new_row.append(row[i] + max(last_row[i], last_row[i+1]))
  triangle[-2] = new_row
  return triangle[:len(triangle)-1]

def tri_sum(triangle):
  while len(triangle) > 1:
    triangle = roll_up(triangle)
  return triangle

f = open('triangle.txt')
tri = []
for line in f:
  tri.append([int(x) for x in line.split(' ')])

print tri_sum(tri)
