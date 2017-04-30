

import click
    
from itertools import permutations
from pathlib import Path

@click.command('59')
@click.option('--verbose', '-v', count=True)
def problem_059(verbose):
    """XOR decryption.

    Each character on a computer is assigned a unique code and the preferred
    standard is ASCII (American Standard Code for Information Interchange).
    For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
    
    A modern encryption method is to take a text file, convert the bytes to
    ASCII, then XOR each byte with a given value, taken from a secret key. The
    advantage with the XOR function is that using the same encryption key on
    the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
    then 107 XOR 42 = 65.
    
    For unbreakable encryption, the key is the same length as the plain text
    message, and the key is made up of random bytes. The user would keep the
    encrypted message and the encryption key in different locations, and
    without both "halves", it is impossible to decrypt the message.
    
    Unfortunately, this method is impractical for most users, so the modified
    method is to use a password as a key. If the password is shorter than the
    message, which is likely, the key is repeated cyclically throughout the
    message. The balance for this method is using a sufficiently long password
    key for security, but short enough to be memorable.
    
    Your task has been made easy, as the encryption key consists of three
    lower case characters. Using
    [cipher.txt](project/resources/p059_cipher.txt) (right click and 'Save
    Link/Target As...'), a file containing the encrypted ASCII codes, and the
    knowledge that the plain text must contain common English words, decrypt
    the message and find the sum of the ASCII values in the original text.
    """

    letters = 'abcdefghijklmnopqrstuvwxyz'
    ordinals = [ord(l) for l in letters]
    keys = permutations(ordinals, 3)
    code = get_encrypted()

    for key in keys:
        decoded = "".join(decrypt(code, key))
        words = decoded.split(' ')
        if len(words) > 50 and 'the' in decoded and 'and' in decoded:
            click.echo("{} ({}): {}".format(
                "".join(chr(k) for k in key),
                sum(ord(l) for l in decoded),   
                "".join(decoded)))



def decrypt(numbers, key):
    return [chr(n ^ key[i % 3]) for i, n in enumerate(numbers)]

def get_encrypted():
    with Path('.', 'files', 'cipher.txt').open('r') as f:
        numbers = f.read()
        return [int(i) for i in numbers.strip().split(',')]
