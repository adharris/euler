
def get_matrix(name):
  lines = open(name).read().splitlines()
  return [[int(i) for i in l.split(',')] for l in lines]

def get_weight(tup, matrix):
  if tup[0] == len(matrix) and tup[1] == len(matrix): return 0
  return matrix[tup[1]][tup[0]]

def get_graph(size):
  return [(-1, -1)] + [(x, y) for x in range(size) for y in range(size)] + [(size, size)]

def get_neighbors(tup, size):
  if tup == (-1, -1):
    return [(0, 0)]
  if tup == (size, size):
    return []
  x = tup[0]
  y = tup[1]
  if x < 0 or x >= size: return []
  if y < 0 or y >= size: return []
  n = []
  #top
  if y > 0:
    n.append((x, y - 1))
  #bottom
  if y < size - 1:
    n.append((x, y + 1))
  #right
  if x < size - 1:
    n.append((x + 1, y))
  #left
  if x > 0:
    n.append((x - 1, y))
  if x == size - 1 and y == size-1:
    n.append((size, size))
  return n

def dijkstra(matrix, start):
  graph = get_graph(len(matrix))
  dist = {}
  previous = {}
  for V in graph:
    dist[V] = float('inf')
    previous[V] = None
  dist[start] = 0
  Q = graph
  while len(Q) > 0:
    Q_dist = { key: dist[key] for key in Q }
    u = min(Q_dist, key=Q_dist.get)
    if dist[u] == float('inf'): break
    Q.remove(u)
    for v in get_neighbors(u, len(matrix)):
      delta = dist[u] + get_weight(v, matrix)
      if delta < dist[v]:
        dist[v] = delta
        previous[v] = u
  return dist
    


matrix = get_matrix('matrix.txt')
small_matrix = [[131, 673, 234, 103, 18],
                [201, 96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524, 37, 331]]

print dijkstra(small_matrix, (-1, -1))[(5,5)] 
print dijkstra(matrix, (-1, -1))[len(matrix), len(matrix)]
