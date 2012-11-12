from pprint import pprint
from copy import deepcopy
from itertools import product

class Edge:
  def __init__(self, node1, node2, weight):
    self.node1 = node1
    self.node2 = node2
    self.weight = weight
  def __str__(self):
    return '{:2} -> {:2} ({:^4})'.format(self.node1, self.node2, self.weight)
  def __eq__(self, other):
    return (self.node1 == other.node1 and self.node2 == other.node2) or (self.node1 == other.node2 and self.node1 == other.node1)

class Network:
  def __init__(self, matrix):
    self.matrix = matrix

  def __str__(self):
    out = ''
    m = self.matrix
    head1 = '  | '
    head2 = '--+-'
    for i in range(len(m)):
      head1 += '{:^4}'.format(i)
      head2 += '----'
    out += head1 + '\n'
    out += head2 + '\n'
    for i in range(len(m)):
      s = '{:2}| '.format(i)
      for j in range(len(m[i])):
        l = '-' if m[i][j] is None else m[i][j]
        s += '{:^4}'.format(l)
      out += s + '\n'
    return out.strip('\n')

  def weight(self):
    return sum(map(lambda x: sum(filter(lambda y: y is not None, x)), self.matrix)) / 2

  def edges(self):
    for i in range(len(self.matrix)):
      for j in range(i, len(self.matrix[i])):
        if self.matrix[i][j] is not None:
          yield Edge(i, j, self.matrix[i][j])

  def edges_from(self, node):
    try:
      node_list = iter(node)
    except:
      node_list = [node]

    for node in node_list:
      for i in range(len(self.matrix)):
        if self.matrix[node][i] is not None:
          yield Edge(node, i, self.matrix[node][i])

  def connected_to(self, node):
    queue = [node]
    visited = [False for i in range(len(self.matrix))]
    while len(queue) > 0:
      next = queue.pop(0)
      unvisted_neighbors = filter(lambda n: not visited[n] and n not in queue, self.edges_from(next))
      queue.extend(unvisted_neighbors)
      visited[next] = True
      for i in range(len(self.matrix)):
        if self.matrix[node][i] is not None:
          yield Edge(node, i, self.matrix[node][i])

      yield next

  def is_connected(self):
    return len(list(self.connected_to(0))) == len(self.matrix)

  def remove_edge(self, edge):
    self.matrix[edge.node1][edge.node2] = None
    self.matrix[edge.node2][edge.node1] = None

  def add_edge(self, edge):
    self.matrix[edge.node1][edge.node2] = edge.weight
    self.matrix[edge.node2][edge.node1] = edge.weight

  def apply_edge_mask(self, mask):
    new = Network(deepcopy(self.matrix))
    for i, edge in enumerate(self.edges()):
      if i >= len(mask):
        break
      if mask[i] == 0:
        new.remove_edge(edge[0], edge[1])
    return new

  def prim(self):
    new = Network([[None for i in range(len(self.matrix))] for j in range(len(self.matrix))])
    tree = [0]
    while len(tree) < len(self.matrix):
      candiate_edges = self.edges_from(tree)
      edges_to_new = filter(lambda e: e.node2 not in tree, candiate_edges)
      shortest_edge = min(edges_to_new, key=lambda e: e.weight)
      new.add_edge(shortest_edge)
      tree.append(shortest_edge.node1 if shortest_edge.node2 in tree else shortest_edge.node2)
    return new

def readNetwork(filename):
  f = open(filename)
  m = []
  for line in f.readlines():
    m.append([None if i == '-' else int(i) for i in line.strip().split(',')])
  return Network(m)

def main():
  net = readNetwork('network.txt')
  mst = net.prim()
  print net
  print mst
  print "new cost: %d" % mst.weight()
  print "saving: %d" % (net.weight() - mst.weight())


if __name__ == '__main__':
  main()