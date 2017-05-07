
from functools import wraps


def memoize(fn):
    memo = {}

    @wraps(fn)
    def decorator(*args):
        if args not in memo:
            memo[args] = fn(*args)
        return memo[args]
    
    return decorator


class Memoize(object):

    def __init__(self, arg_count=None):
        self.arg_count = arg_count
        self.cache = dict()
        
    def get_cache_key(self, args, kwargs):

        if self.arg_count is not None:
            return args[:self.arg_count]
        
        return (args, kwargs.items())


    def __call__(self, fn):

        @wraps(fn)
        def decorator(*args, **kwargs):
            key = self.get_cache_key(args, kwargs)
            if key not in self.cache:
                self.cache[key] = fn(*args, **kwargs)
            return self.cache[key]

        decorator.memoize = self

        return decorator
    
    def clear_cache(self):
        self.cache.clear()