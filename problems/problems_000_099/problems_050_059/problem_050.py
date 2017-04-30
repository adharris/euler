

import click

from tools.primes import sieve_of_eratosthenes


@click.command('50')
@click.option('--verbose', '-v', count=True)
def problem_050(verbose):
    """Consecutive prime sum.

    The prime 41, can be written as the sum of six consecutive primes:
    
    41 = 2 + 3 + 5 + 7 + 11 + 13
    
    This is the longest sum of consecutive primes that adds to a prime below
    one-hundred.
    
    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.
    
    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
    
    """

    primes = sieve_of_eratosthenes(1000000)
    sets = generate_prime_lists(primes)
    longest = max(sets, key=lambda s: s[1])
    print(longest)


def generate_prime_lists(primes):
    prime_set = set(primes)
    largest = primes[-1]

    for i, prime in enumerate(primes):
        for j in range(i + 1, len(primes)):
            total = sum(primes[i:j+1])
            
            if total > largest:
                break

            if total in prime_set:
                yield (i, j -i + 1, prime, total, primes[i:j+1])