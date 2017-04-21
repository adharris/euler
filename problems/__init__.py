
from itertools import chain
from .problems_000_099 import all_commands as problems_000_099

all_commands = list(chain(
    problems_000_099,
))

__all__ = ['all_commands']