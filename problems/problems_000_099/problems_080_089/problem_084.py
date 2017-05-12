

import click

from collections import Counter
from random import randint, shuffle


@click.command('84')
@click.option('--sides', '-s', type=int, default=4)
@click.option('--verbose', '-v', count=True)
def problem_084(sides, verbose):
    """Monopoly odds.

    In the game, _Monopoly_, the standard board is set up in the following
    way:
    
    GO  | A1 | CC1 | A2 | T1 | R1 | B1 | CH1 | B2 | B3 | JAIL  
    ----|----|-----|----|----|----|----|-----|----|----|---  
    H2  |                                              | C1  
    T2  |                                              | U1  
    H1  |                                              | C2  
    CH3 |                                              | C3  
    R4  |                                              | R2  
    G3  |                                              | D1  
    CC3 |                                              | CC2  
    G2  |                                              | D2  
    G1  |                                              | D3  
    G2J | F3 | U2 | F2 | F1 | R3 | E3 | E2 | CH2 | E1  | FP  
      
    A player starts on the GO square and adds the scores on two 6-sided dice
    to determine the number of squares they advance in a clockwise direction.
    Without any further rules we would expect to visit each square with equal
    probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
    chest), and CH (chance) changes this distribution.
    
    In addition to G2J, and one card from each of CC and CH, that orders the
    player to go directly to jail, if a player rolls three consecutive
    doubles, they do not advance the result of their 3rd roll. Instead they
    proceed directly to jail.
    
    At the beginning of the game, the CC and CH cards are shuffled. When a
    player lands on CC or CH they take a card from the top of the respective
    pile and, after following the instructions, it is returned to the bottom
    of the pile. There are sixteen cards in each pile, but for the purpose of
    this problem we are only concerned with cards that order a movement; any
    instruction not concerned with movement will be ignored and the player
    will remain on the CC/CH square.
    
      * Community Chest (2/16 cards): 
        1. Advance to GO
        2. Go to JAIL
      * Chance (10/16 cards): 
        1. Advance to GO
        2. Go to JAIL
        3. Go to C1
        4. Go to E3
        5. Go to H2
        6. Go to R1
        7. Go to next R (railway company)
        8. Go to next R
        9. Go to next U (utility company)
        10. Go back 3 squares.
    
    The heart of this problem concerns the likelihood of visiting a particular
    square. That is, the probability of finishing at that square after a roll.
    For this reason it should be clear that, with the exception of G2J for
    which the probability of finishing on it is zero, the CH squares will have
    the lowest probabilities, as 5/8 request a movement to another square, and
    it is the final square that the player finishes at on each roll that we
    are interested in. We shall make no distinction between "Just Visiting"
    and being sent to JAIL, and we shall also ignore the rule about requiring
    a double to "get out of jail", assuming that they pay to get out on their
    next turn.
    
    By starting at GO and numbering the squares sequentially from 00 to 39 we
    can concatenate these two-digit numbers to produce strings that correspond
    with sets of squares.
    
    Statistically it can be shown that the three most popular squares, in
    order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
    (3.09%) = Square 00. So these three most popular squares can be listed
    with the six-digit modal string: 102400.
    
    If, instead of using two 6-sided dice, two 4-sided dice are used, find the
    six-digit modal string.
    
    """

    board = Board(sides)
    common = board.find_most_common(3)
    click.echo(common)


def go_back_3(index):
    return (index - 3) % 40


def go_to_next_railroad(index):
    return (((index + 5) // 10) * 10 + 5) % 40


def go_to_next_utility(index):
    if index < 12:
        return 12
    if index < 28:
        return 28
    return 12


class Board(object):

    def __init__(self, die_sides):
        self.die_sides = die_sides
        self.chance = Chance()
        self.community = CommunityChest()
        self.location = 0
        self.visits = Counter()
        self.double_count = 0

    def find_most_common(self, n):
        self.do_n_moves(1000000)
        return self.get_most_common(n)
    
    def roll(self):
        one = randint(1, self.die_sides)
        two = randint(1, self.die_sides)
        return (one + two, one == two)

    def get_most_common(self, n):
        return tuple(k for k, v in self.visits.most_common(n))
    
    def do_n_moves(self, n):
        for n in range(n):
            self.do_move()
        
    def do_move(self):
        val, double = self.roll()

        if double:
            self.double_count += 1
        else:
            self.double_count = 0
        
        if self.double_count == 3:
            self.double_count = 0
            
        loc = self.location + val
        loc %= 40

        if loc == 7 or loc == 22 or loc == 36:
            loc = self.chance.draw_and_apply_card(loc)
            
        if loc == 2 or loc == 17 or loc == 33:
            loc = self.community.draw_and_apply_card(loc)
        
        if loc == 30:
            loc = 10

        self.visits[loc] += 1
        self.location = loc


class Deck(object):

    def __init__(self, cards):
        self.cards = cards
        self.index = 0
        shuffle(self.cards)

    def draw_and_apply_card(self, location):
        card = self.cards[self.index]
        self.index += 1
        self.index %= len(self.cards)
        
        if card is None:
            return location
            
        if isinstance(card, int):
            return card
        
        return card(location)


class CommunityChest(Deck):

    def __init__(self):
        blank = [None] * 14
        cards = [0, 10]
        super().__init__(cards + blank)


class Chance(Deck):
    def __init__(self):
        blank = [None] * 6
        dest = [0, 10, 11, 24, 39, 5]
        fns = [go_to_next_railroad, go_to_next_railroad, go_to_next_utility,
               go_back_3]
        super().__init__(fns + blank + dest)

