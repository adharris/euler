

import click
from tools.numbers import digit_count

@click.command('36')
@click.option('--limit', '-l', type=int, default=1000000)
@click.option('--verbose', '-v', count=True)
def problem_036(limit,verbose):
    """Double-base palindromes.

    The decimal number, 585 = 10010010012 (binary), is palindromic in both
    bases.
    
    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.
    
    (Please note that the palindromic number, in either base, may not include
    leading zeros.)
    
    """

    # 999,999 has 20 base 2 digits, so we need to generate all 10 digit
    # binary strings which is 2**10 = 1024 palindromes

    # 999,999 has 6 base 10 digits, so we need to generate 3 digit
    # strings, wich is 1000. There are _slighly_ fewer base 10 palindromes

    palindromes = (p for n in range(1, 1000) for p in make_palindromes(n))
    base2 = (format(int(p), 'b') for p in palindromes)
    double_base = [(int(b, 2), b) for b in base2 if is_palindrome(b)]
    
    if verbose > 0:
        double_base.sort()
        longest = max(digit_count(n[0]) for n in double_base)
        lines = ("{:{}}:{}".format(d, longest, b) for d, b in double_base)
        click.echo('\n'.join(lines))

    click.echo(sum(d for d, b in double_base))

def make_palindromes(string):
    string = str(string)
    yield string + string[::-1]
    yield string + string[:-1][::-1]


def is_palindrome(string):
    string = str(string)
    to_mirror = len(string) // 2
    return string.endswith(string[:to_mirror][::-1])