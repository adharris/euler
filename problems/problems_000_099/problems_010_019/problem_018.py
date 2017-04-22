
import click

from itertools import chain
from tools.numbers import digit_count
from collections import defaultdict

@click.command('18')
def problem_018():
    """Maximum path sum I

    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.
    
    **3**  
    **7** 4  
    2 **4** 6  
    8 5 **9** 3
    
    That is, 3 + 7 + 4 + 9 = 23.
    
    Find the maximum total from top to bottom of the triangle below:
    """

    # I use the recursive algorithm here, but its not the right way!

    raw_triangle = """
        75  
        95 64  
        17 47 82  
        18 35 87 10  
        20 04 82 47 65  
        19 01 23 75 03 34  
        88 02 77 73 07 63 67  
        99 65 04 28 06 16 70 92  
        41 41 26 56 83 40 80 70 33  
        41 48 72 33 47 32 37 16 94 29  
        53 71 44 65 25 43 91 52 97 51 14  
        70 11 33 28 77 73 17 78 39 68 17 57  
        91 71 52 38 17 14 91 43 58 50 27 29 48  
        63 66 04 68 89 53 67 30 73 16 69 87 40 31  
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
        """

    print_shortest_and_longest(raw_triangle)


def print_shortest_and_longest(raw_triangle):

    triangle = parse_triangle(raw_triangle)
    longest = find_path(triangle, longer_path)
    shortest = find_path(triangle, shorter_path)
    print_triangle(triangle, red=longest[1], green=shortest[1])
    click.secho('Longest Path {}'.format(longest[0]), fg='red')
    click.secho('Shortest Path {}'.format(shortest[0]), fg='green')


def find_path(triangle, pick_path):
    apex = triangle[0][0]

    if len(triangle) == 1:
        return (apex, (0, ))
    
    left, right = split_triangle(triangle)
    left_path = find_path(left, pick_path)
    right_path = find_path(right, pick_path)
    
    next_path = pick_path(left_path, right_path)
    return add_apex_to_path(next_path, apex, next_path is right_path)


def longer_path(left, right):
    return left if left[0] > right[0] else right


def shorter_path(left, right):
    return left if left[0] < right[0] else right


def add_apex_to_path(path, apex, is_left):
    new_total = path[0] + apex
    new_path = path[1] if is_left else tuple(i + 1 for i in path[1])
    return (new_total, (0, ) + new_path)

def split_triangle(triangle):
    left = [line[:-1] for line in triangle[1:]]
    right = [line[1:] for line in triangle[1:]]
    return left, right


def parse_triangle(raw):
    return [
        [int(v) for v in line.strip().split()]
        for line in raw.strip().splitlines()]


def print_triangle(triangle, **highlights):

    length = len(triangle[-1])
    digits = max(digit_count(n) for n in chain.from_iterable(triangle))
    pad = " " * (digits // 2 + 1)
    sep = " " if digits % 2 == 1  else "  "

    highlights = make_highlights(highlights)

    for i, row in enumerate(triangle):
        strs = row_to_strings(row, 2)
        strs = format_row(strs, highlights.get(i, {}))
        joined = sep.join(strs)
        padding = pad * (length - len(row))
        click.echo(padding +'{0}'.format(joined)) 


def make_highlights(highlights):
    result = defaultdict(dict)
    for color, path in highlights.items():
        for row, value in enumerate(path):
            result[row][value] = color
    return result


def row_to_strings(row, digits):
    return ['{0:0{1}d}'.format(r, digits) for r in row]


def format_row(row, highlights):
    return [click.style(s, fg=highlights.get(i, 'white'))
            for i, s in enumerate(row)]