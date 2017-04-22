
from functools import wraps


def memoize(fn):
    memo = {}

    @wraps(fn)
    def decorator(*args):
        if args not in memo:
            memo[args] = fn(*args)
        return memo[args]
    
    return decorator