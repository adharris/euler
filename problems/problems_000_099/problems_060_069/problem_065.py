
import click
from fractions import Fraction
from tools.numbers import iter_digits


@click.command('65')
@click.option('--limit', '-l', type=int, default=100)
@click.option('--verbose', '-v', count=True)
def problem_065(limit,verbose):
    """Convergents of e.

    The square root of 2 can be written as an infinite continued fraction.

    The infinite continued fraction can be written, √2 = [1;(2)], (2)
    indicates that 2 repeats _ad infinitum_. In a similar way, √23 =
    [4;(1,3,1,8)].
    
    It turns out that the sequence of partial values of continued fractions
    for square roots provide the best rational approximations. Let us consider
    the convergents for √2.
      
    Hence the sequence of the first ten convergents for √2 are:
    
    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378,
    ...
    
    What is most surprising is that the important mathematical constant,  
    _e_ = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2_k_,1, ...].
    
    The first ten terms in the sequence of convergents for _e_ are:
    
    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
    
    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
    
    Find the sum of digits in the numerator of the 100th convergent of the
    continued fraction for _e_.
    
    """

    convergent = get_nth_convergent(limit - 1)
    numerator_digits = iter_digits(convergent.numerator)   
    click.echo(sum(numerator_digits))


def get_nth_coefficient(n):
    if n == 0:
        return 2
    if n % 3 == 2:
        return ((n + 1) // 3) * 2
    return 1


def get_nth_convergent(n):
    fraction = 0
    for i in range(n, 0, -1):
        fraction = Fraction(1, (get_nth_coefficient(i) + fraction))
    return get_nth_coefficient(0) + fraction