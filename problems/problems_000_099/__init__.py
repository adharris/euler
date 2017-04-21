
from itertools import chain
from .problems_010_019 import all_commands as problems_010_019
from .problems_000_009 import all_commands as problems_000_009

all_commands = list(chain(
    problems_010_019,
    problems_000_009,
))

__all__ = ['all_commands']