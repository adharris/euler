

import click

from tools.primes import unbounded_sieve_of_eratosthenes
from tools.numbers import digit_count


@click.command('37')
@click.option('--verbose', '-v', count=True)
def problem_037(verbose):
    """Truncatable primes.

    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain
    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
    right to left: 3797, 379, 37, and 3.
    
    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.
    
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    
    """

    found_primes = set()
    truncatable_primes = set()

    def is_truncatable(prime):
        if prime < 10:
            return False

        for truncaction in truncactions(prime):
            if truncaction not in found_primes:
                return False
        return True

    for prime in unbounded_sieve_of_eratosthenes(100000):
        found_primes.add(prime)
        
        if is_truncatable(prime):
            truncatable_primes.add(prime)

        if len(truncatable_primes) >= 11:
            break
    
    click.echo(",".join(str(p) for p in sorted(truncatable_primes)))
    click.echo(sum(truncatable_primes))


def truncactions(number):
    digits = digit_count(number)
    for i in range(digits - 1):
        yield number % (10 ** (digits - i - 1))
        yield number // 10 ** (i + 1)