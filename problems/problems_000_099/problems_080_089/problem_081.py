

import click

from collections import namedtuple, defaultdict
from tools.numbers import digit_count

from pathlib import Path


@click.command('81')
@click.option('--verbose', '-v', count=True)
def problem_081(verbose):
    """Path sum: two ways.

    In the 5 by 5 matrix below, the minimal path sum from the top left to the
    bottom right, by **only moving to the right and down**, is indicated in
    bold red and is equal to 2427.
    
    Find the minimal path sum, in
    [matrix.txt](project/resources/p081_matrix.txt) (right click and "Save
    Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from
    the top left to the bottom right by only moving right and down.
    """

    graph = Graph.from_file()
    d, v = graph.find_path()
    print(d[graph.end])



Node = namedtuple('Node', "value connected")


class Point(namedtuple('Point', 'x y')):

    @property
    def right(self):
        return Point(self.x + 1, self.y)

    @property
    def left(self):
        return Point(self.x - 1, self.y)
    
    @property
    def above(self):
        return Point(self.x, self.y - 1)

    @property
    def below(self):
        return Point(self.x, self.y + 1)
 


class Graph(object):

    def __init__(self, raw):
    
        self.start = object()
        self.end = object()

        self.nodes = self.parse_raw_values(raw)

        last = max(self.nodes)
        self.width = last.x + 1
        self.height = last.y + 1

        self.edges = self.parse_edges(self.nodes)
        
    def parse_raw_values(self, raw):
        return {
            Point(x, y): int(v.strip())
            for y, line in enumerate(raw.strip().splitlines())
            for x, v in enumerate(line.strip().split(','))}
    
    def parse_edges(self, nodes):
        edges = defaultdict(set)
        start = set(self.get_start_nodes())
        end = set(self.get_end_nodes())

        for source in nodes.keys():

            for dest in self.get_edges(source):
                if dest in nodes:
                    edges[source].add(dest)
            
            if source in start:
                edges[self.start].add(source)

            if source in end:
                edges[source].add(self.end)

        return edges

    def get_edges(self, point):
        yield point.right
        yield point.below

    def get_start_nodes(self):
        yield (0, 0)

    def get_end_nodes(self):
        yield (self.width - 1, self.height - 1)
        
    def shortest_path(self):
        return self.find_path()[0][self.end]
        
    def print(self):
        d, p = self.find_path()
        path = [self.end]
        longest = max(digit_count(v) for v in self.nodes.values())

        while p[path[-1]]:
            path.append(p[path[-1]])

        result = ""
        for y in range(self.height):
            for x in range(self.width):
                p = (x, y)
                fg = 'red' if p in path else 'white'
                s = "{:{}} ".format(self.nodes[p], longest)
                result += click.style(s, fg=fg)
            result += '\n'
        click.echo_via_pager(result)
                

    def find_path(self):

        unvisited = set(self.nodes.keys())
        distances = defaultdict(lambda: float('inf'))
        previous = defaultdict(lambda: None)
        
        unvisited.add(self.start)
        unvisited.add(self.end)
        
        distances[self.start] = 0

        while unvisited:
            closest = min(unvisited, key=lambda p: distances[p])
            unvisited.remove(closest)

            for neighbor in self.edges[closest]:
                distance = distances[closest] + self.nodes.get(neighbor, 0)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = closest

        return distances, previous

    
    @classmethod
    def test(cls):
        return cls("""
            131, 673, 234, 103, 18
            201, 96, 342, 965, 150
            630, 803, 746, 422, 111
            537, 699, 497, 121, 956
            805, 732, 524, 37, 331""")
    
    @classmethod
    def from_file(cls):
        with Path('.', 'files', 'matrix.txt').open('r') as f:
            return cls(f.read())


def a_star(start, end):

    closed_set = set()
    
    open_set = set(start)

    came_from = dict()

    g_score = defaultdict(lambda: float('inf'))

    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
