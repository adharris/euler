
import click
from tools.numbers import iter_digits

@click.command('30')
@click.option('--power', '-p', type=int, default=5)
def problem_030(power):
    """Digit fifth powers

    Surprisingly there are only three numbers that can be written as the sum
    of fourth powers of their digits:
    
    > 1634 = 14 \+ 64 \+ 34 \+ 44  
    >  8208 = 84 \+ 24 \+ 04 \+ 84  
    >  9474 = 94 \+ 44 \+ 74 \+ 44
    
    As 1 = 14 is not a sum it is not included.
    
    The sum of these numbers is 1634 + 8208 + 9474 = 19316.
    
    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
    
    """

    upper = 10 ** (power + 1)
    numbers =  (n for n in range(2, upper) 
                if digit_power_sum(n, power) == n)
    click.echo(sum(numbers))
    

def digit_power_sum(number, power):
    return sum(d ** power for d in iter_digits(number)) 