

import click

@click.command('14')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_014(limit, verbose): 
    """Longest Collatz sequence

    The following iterative sequence is defined for the set of positive
    integers:
    
    n → n/2 (n is even)  
    n → 3n \+ 1 (n is odd)
    
    Using the rule above and starting with 13, we generate the following
    sequence:
    
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.
    
    Which starting number, under one million, produces the longest chain?
    
    **NOTE:** Once the chain starts the terms are allowed to go above one million.
    
    """

    collatz = CollatzMemoizer()

    with click.progressbar(range(1, limit)) as bar:
        lengths = ((collatz.get_length(n), n) for n in bar)
        longest = max(lengths)
    
    if verbose >= 1:
        click.echo(' → '.join(str(s) for s in collatz(longest[1])))

    print(len(collatz.lengths))

    click.echo("{1} has a Collatz length of {0}".format(*longest))


class CollatzMemoizer(object):

    def __init__(self):
        self.lengths = {1: 1}

    def get_length(self, number):
        if number in self.lengths:
            return self.lengths[number]

        next_in_sequence = next_collatz(number)
        length = self.get_length(next_in_sequence) + 1
        self.lengths[number] = length
        
        return length
        
        
        
def next_collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def collatz(n):
    while n != 1:
        n = next_collatz(n)
        yield n
    yield 1

def collatz_length(n):
    length = 1
    while n != 1:
        n = next_collatz(n)
        length += 1
    return length