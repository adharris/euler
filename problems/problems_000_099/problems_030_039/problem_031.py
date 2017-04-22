

import click

from itertools import islice
from tools.memoization import memoize

@click.command('31')
@click.option('--total', '-t', type=int, default=200)
@click.option('--verbose', '-v', count=True)
def problem_031(total, verbose):
    """Coin sums

    In England the currency is made up of pound, £, and pence, p, and there
    are eight coins in general circulation:
    
    > 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    
    It is possible to make £2 in the following way:
    
    > 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    
    How many different ways can £2 be made using any number of coins?
    
    """
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    
    def format_coin_value(amt, count):
        sym = "£" if amt >= 100 else 'p'
        amt = amt // 100 if amt >= 100 else amt
        return '{}×{}{}'.format(count, amt, sym)
    
    def total_combo(combo):
        return sum(a * v for a, v in combo)

    def format_combo(combo):
        filtered = (c for c in combo if c[1] > 0)
        formatted = (format_coin_value(*c) for c in filtered)
        total = sum(a * v for a, v in combo)
        return " + ".join(formatted) + " = {}".format(total) 

    def format_combos(combos):
        formatted = (format_combo(c) for c in combos)
        return "\n".join(formatted)

    combos = iterate_combinations(total, coins)
    if verbose >= 1:
        click.echo_via_pager(format_combos(combos))
    else:
        click.echo(len(list(combos)))
        

def iterate_combinations(total, coins):
    coin_value = coins[0]

    if total == 0:
        yield ()
        return
    
    if coin_value == 1:
        yield ((1, total), )
        return
        
    max_possible = total // coin_value

    for coin_count in range(0, max_possible + 1):
        used = coin_count * coin_value
        remaining = total - used
        for combo in iterate_combinations(remaining, coins[1:]):
            yield ((coin_value, coin_count), ) + combo