
import click

from pathlib import Path

@click.command('22')
def problem_022():
    """Names scores

    Using [names.txt](project/resources/p022_names.txt) (right click and 'Save
    Link/Target As...'), a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical
    position in the list to obtain a name score.
    
    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.
    
    What is the total of all the name scores in the file?
    """

    path = Path('.', 'files', 'names.txt')
    with path.open('r') as f:
        names = f.read()

    names = names[1:-1].split('","')
    names.sort()
    scores = (name_score(name, i + 1) for i, name in enumerate(names))
    click.echo(sum(scores))

def name_score(name, position):
    return sum(ord(n) - 64 for n in name) * position
