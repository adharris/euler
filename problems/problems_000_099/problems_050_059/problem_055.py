

import click

@click.command('55')
@click.option('--limit', '-l', type=int, default=10000)
@click.option('--iterations', '-i', type=int, default=50)
@click.option('--verbose', '-v', count=True)
def problem_055(limit, iterations, verbose):
    """Lychrel numbers.

    If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
    
    Not all numbers produce palindromes so quickly. For example,
    
    349 + 943 = 1292,  
    1292 + 2921 = 4213  
    4213 + 3124 = 7337
    
    That is, 349 took three iterations to arrive at a palindrome.
    
    Although no one has proved it yet, it is thought that some numbers, like
    196, never produce a palindrome. A number that never forms a palindrome
    through the reverse and add process is called a Lychrel number. Due to the
    theoretical nature of these numbers, and for the purpose of this problem,
    we shall assume that a number is Lychrel until proven otherwise. In
    addition you are given that for every number below ten-thousand, it will
    either (i) become a palindrome in less than fifty iterations, or, (ii) no
    one, with all the computing power that exists, has managed so far to map
    it to a palindrome. In fact, 10677 is the first number to be shown to
    require over fifty iterations before producing a palindrome:
    4668731596684224866951378664 (53 iterations, 28-digits).
    
    Surprisingly, there are palindromic numbers that are themselves Lychrel
    numbers; the first example is 4994.
    
    How many Lychrel numbers are there below ten-thousand?
    
    NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
    theoretical nature of Lychrel numbers.
    
    """

    lychrel_numbers = [n for n in range(limit) if is_lychrel(n, iterations)]
    click.echo(len(lychrel_numbers))


def is_lychrel(number, max_iterations):
    for i in range(max_iterations):
        number = transform(number)
        if is_palindromic_number(number):
            return False
    return True


def transform(number):
    return number + int("".join(reversed(str(number))))


def is_palindromic_number(number):
    as_string = str(number)
    length = len(as_string)
    for index in range(0, length // 2):
        if as_string[index] != as_string[length - 1 - index]:
            return False
    return True