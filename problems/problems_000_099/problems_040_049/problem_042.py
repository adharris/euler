

import click

from tools.series import triangle_numbers
from pathlib import Path
from itertools import takewhile

@click.command('42')
@click.option('--verbose', '-v', count=True)
def problem_042(verbose):
    """Coded triangle numbers.

    The _n_th term of the sequence of triangle numbers is given by, _tn_ =
    ½_n_(_n_+1); so the first ten triangle numbers are:
    
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    
    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = _t_10. If the word
    value is a triangle number then we shall call the word a triangle word.
    
    Using [words.txt](project/resources/p042_words.txt) (right click and 'Save
    Link/Target As...'), a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?
    
    """

    with Path('.', 'files', 'words.txt').open('r') as f:
        words = f.read()
        words = [w[1:-1] for w in words.split(',')]
        
    scores = [(word_score(word), word) for word in words]
    largest_score = max(scores)
    
    triangles = takewhile(lambda n: n <= largest_score[0], triangle_numbers())
    triangles = set(triangles)
    
    triangle_words = [word for word in scores if word[0] in triangles]

    if verbose:
        triangle_words.sort(key=lambda w: w[1])
        for word in triangle_words:
            click.echo('{} {}'.format(*word))
    
    click.echo(len(triangle_words))



def word_score(string):
    return sum(ord(s) - 64 for s in string)

