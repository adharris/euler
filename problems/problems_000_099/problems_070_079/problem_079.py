

import click

from pathlib import Path
from collections import deque

@click.command('79')
@click.option('--verbose', '-v', count=True)
def problem_079(verbose):
    """Passcode derivation.

    A common security method used for online banking is to ask the user for
    three random characters from a passcode. For example, if the passcode was
    531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
    reply would be: 317.
    
    The text file, [keylog.txt](project/resources/p079_keylog.txt), contains
    fifty successful login attempts.
    
    Given that the three characters are always asked for in order, analyse the
    file so as to determine the shortest possible secret passcode of unknown
    length.
    
    """

    keys = load_keys()
    rules = set(generate_rules(keys))
    codes = {""}

    for rule in sorted(rules):
        codes = apply_rule_to_codes(codes, rule)
        shortest = len(min(codes, key=lambda s: len(s)))
        codes = [c for c in codes if len(c) <= shortest]

    print(min(codes, key=lambda s: len(s)))

def generate_rules(keys):
    for key in keys:
        yield (key[0], key[1])
        yield (key[0], key[2])
        yield (key[1], key[2])
        

def apply_rule_to_codes(codes, rule):
    return {applied for code in codes for applied in apply_rule(code, rule)}


def apply_rule(code, rule):
    index_1 = code.find(rule[0])
    index_2 = code.find(rule[1])
    
    if index_1 >= 0 and index_2 >= 0 and index_1 < index_2:
        # Rule is fulfilled already
        return (code, )
    
    if index_1 >= 0:
        # Append char_2 to all locations after char_1
        return tuple(
            insert_char_at(code, rule[1], i)
            for i in range(index_1 + 1, len(code) + 1))
    
    if index_2 >= 0:
        # Insert char 1 at all locations before char 2
        return tuple(
            insert_char_at(code, rule[0], i)
            for i in range(0, index_2 + 1))
    
    # Insert both chars in all ways that the first is before the second
    codes = deque()

    for i in range(0, len(code) + 1):
        first_sub = insert_char_at(code, rule[0], i)
        for j in range(i + 1, len(first_sub) + 1):
            codes.append(insert_char_at(first_sub, rule[1], j))

    return tuple(codes)

def insert_char_at(string, char, index):
    return string[:index] + char +  string[index:]

def load_keys():
    with Path('.', 'files', 'keylog.txt').open('r') as f:
        return [line.strip() for line in f.readlines()]
