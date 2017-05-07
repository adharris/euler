
from itertools import chain
from .problems_010_019 import all_commands as problems_010_019
from .problems_020_029 import all_commands as problems_020_029
from .problems_030_039 import all_commands as problems_030_039
from .problems_000_009 import all_commands as problems_000_009
from .problems_060_069 import all_commands as problems_060_069
from .problems_070_079 import all_commands as problems_070_079
from .problems_040_049 import all_commands as problems_040_049
from .problems_050_059 import all_commands as problems_050_059
from .problems_080_089 import all_commands as problems_080_089

all_commands = list(chain(
    problems_010_019,
    problems_020_029,
    problems_030_039,
    problems_000_009,
    problems_060_069,
    problems_070_079,
    problems_040_049,
    problems_050_059,
    problems_080_089,
))

__all__ = ['all_commands']