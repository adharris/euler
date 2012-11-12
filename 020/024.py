from itertools import permutations

perms = list(permutations('0123456789'))
perms = map(lambda x: ''.join(x), perms)
print sorted(perms)[999999]
