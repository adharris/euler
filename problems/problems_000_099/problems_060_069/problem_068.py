

import click

@click.command('68')
@click.option('--sides', '-s', type=int, default=5)
@click.option('--verbose', '-v', count=True)
def problem_068(sides,verbose):
    """Magic 5-gon ring.

    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
    and each line adding to nine.
    
        4
         \
          3
         / \
        1---2---6
       /
      5

    Working **clockwise**, and starting from the group of three with the
    numerically lowest external node (4,3,2 in this example), each solution
    can be described uniquely. For example, the above solution can be
    described by the set: 4,3,2; 6,2,1; 5,1,3.
    
    It is possible to complete the ring with four different totals: 9, 10, 11,
    and 12. There are eight solutions in total.
    
    **Total**| **Solution Set**  
    ---|---  
    9|  4,2,3; 5,3,1; 6,1,2  
    9|  4,3,2; 6,2,1; 5,1,3  
    10| 2,3,5; 4,5,1; 6,1,3  
    10| 2,5,3; 6,3,1; 4,1,5  
    11| 1,4,6; 3,6,2; 5,2,4  
    11| 1,6,4; 5,4,2; 3,2,6  
    12| 1,5,6; 2,6,4; 3,4,5  
    12| 1,6,5; 3,5,4; 2,4,6  
      
    By concatenating each group it is possible to form 9-digit strings; the
    maximum string for a 3-gon ring is 432621513.
    
    Using the numbers 1 to 10, and depending on arrangements, it is possible
    to form 16- and 17-digit strings. What is the maximum **16-digit** string
    for a "magic" 5-gon ring?
    
    ![](project/images/p068_2.gif)  
    
    """
    nodes = sides * 2
    ring = [None] * nodes

    # This can be solved directly, using logic. This produces solutions for
    # quickly for N-gons with up to 10**8, but the output text is 208 megabytes.

    # We want the largest numbers on the outside, so we calulate the total of
    # each triplet:
    outer_ring = range(sides + 1, nodes + 1)
    inner_ring = range(1, sides + 1)
    total = (sum(inner_ring) * 2 + sum(outer_ring)) // sides

    # Since we always start with the smallest external node in enumeration,
    # the first node should always be the smallest of outer rings
    set_node(ring, 0, 0, min(outer_ring))

    # The first inner value is the largest of the inner ring:
    set_node(ring, 0, 1, max(inner_ring))

    # The second inner ring is can be solved for:
    solve(ring, 0, total)

    click.echo(get_triplet_string(ring, 0), nl=False)

    # Now, we can fill the remaining outer nodes with the largest remaing outer
    # values, and solve the the inner values
    for i in range(1, sides):
        set_node(ring, i, 0, outer_ring[-i])
        solve(ring, i, total)
        click.echo(get_triplet_string(ring, i), nl=i == sides - 1)
    


def ring_total(inner_ring, outer_ring):
    return (sum(inner_ring) * 2 + sum(outer_ring)) // len(inner_ring)


def solve(ring, item, total):
    value = total - get_node(ring, item, 0) - get_node(ring, item, 1)
    set_node(ring, item, 2, value)


def get_triplet_string(ring, item):
    return "".join(str(i) for i in get_triplet(ring, item))


def get_triplet(ring, item):
    return (
        get_node(ring, item, 0), 
        get_node(ring, item, 1), 
        get_node(ring, item, 2))


def generate_triplets(ring):
    sides = len(ring) // 2
    return tuple((
        ring[i],
        ring[sides + i],
        ring[sides + (i + 1) % sides]
    ) for i in range(sides))


def set_node(ring, item, position, value):
    size = len(ring) // 2
    if position == 0:
        ring[item] = value
    if position == 1:
        ring[size + item] = value
    if position == 2:
        ring[size + (item + 1) % size] = value


def get_node(ring, item, position):
    size = len(ring) // 2
    if position == 0:
        return ring[item]
    if position == 1:
        return ring[size + item]
    if position == 2:
        return ring[size + (item + 1) % size]


def set_tuple_index(ring, index, value):
    return ring[:index] + (value, ) + ring[index + 1:]

 