

import click

from itertools import permutations

@click.command('38')
@click.option('--digit', '-d', type=int, default=9)
@click.option('--verbose', '-v', count=True)
def problem_038(digit, verbose):
    """Pandigital multiples.

    Take the number 192 and multiply it by each of 1, 2, and 3:
    
    > 192 × 1 = 192  
    > 192 × 2 = 384  
    > 192 × 3 = 576
    
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and (1,2,3)
    
    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).
    
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """

    digits = "987654321"
    pandigitals = ("".join(p) for p in permutations(digits))
    
    for pandigital in pandigitals:
        for partition in all_partitions(pandigital):
            n = find_n(partition)
            if n is not None:
                click.echo((pandigital, partition, n))
                return


def find_n(numbers):
    first = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] / (i + 1) != first:
            return None
    return first

def all_partitions(string):
    return (p for n in range(2, 10) for p in n_partitions(string, n))   


def n_partitions(string, n):
    if len(string) < n:
        return
        
    if n <= 1:
        yield (int(string), )
        return

    for i in range(1, len(string)):
        for p in n_partitions(string[i:], n - 1):
            yield (int(string[:i]), ) + p