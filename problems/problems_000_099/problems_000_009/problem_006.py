
import click


@click.command('6')
@click.option('--limit', '-l', type=int, default=100)
def problem_006(limit):
    """Sum square difference.

    Both expressions have a closed form, so this is constant time.
    
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    
    Hence the difference between the sum of the squares of the first ten 
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one 
    hundred natural numbers and the square of the sum.
    """

    # Sum of numbers (n(n+1)) / 2
    square_of_sum = ((limit * (limit + 1)) / 2) ** 2

    # Sum of squares (n(n+1)(2n+1))/6
    sum_of_squares = (limit * (limit + 1) * (2 * limit + 1)) / 6

    click.echo('Square of sum: {}'.format(square_of_sum))
    click.echo('Sum of squares: {}'.format(sum_of_squares))
    click.echo('Difference: {}'.format(square_of_sum - sum_of_squares))

