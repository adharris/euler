

import click

from collections import namedtuple, Counter
from pathlib import Path


@click.command('54')
@click.option('--verbose', '-v', count=True)
def problem_054(verbose):
    """Poker hands.

    In the card game poker, a hand consists of five cards and are ranked, from
    lowest to highest, in the following way:
    
      * **High Card**: Highest value card.
      * **One Pair**: Two cards of the same value.
      * **Two Pairs**: Two different pairs.
      * **Three of a Kind**: Three cards of the same value.
      * **Straight**: All cards are consecutive values.
      * **Flush**: All cards of the same suit.
      * **Full House**: Three of a kind and a pair.
      * **Four of a Kind**: Four cards of the same value.
      * **Straight Flush**: All cards are consecutive values of same suit.
      * **Royal Flush**: Ten, Jack, Queen, King, Ace, in same suit.
    
    The cards are valued in the order:  
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
    
    If two players have the same ranked hands then the rank made up of the
    highest value wins; for example, a pair of eights beats a pair of fives
    (see example 1 below). But if two ranks tie, for example, both players
    have a pair of queens, then highest cards in each hand are compared (see
    example 4 below); if the highest cards tie then the next highest cards are
    compared, and so on.
    
    Consider the following five hands dealt to two players:
    
    **Hand**|  | **Player 1**|  | **Player 2**|  | **Winner**  
    ---|---|---|---|---|---|---  
    **1**|  | 5H 5C 6S 7S KD  
    
    Pair of Fives
    
    |  | 2C 3S 8S 8D TD  
    
    Pair of Eights
    
    |  | Player 2  
    **2**|  | 5D 8C 9S JS AC  
    
    Highest card Ace
    
    |  | 2C 5C 7D 8S QH  
    
    Highest card Queen
    
    |  | Player 1  
    **3**|  | 2D 9C AS AH AC  
    
    Three Aces
    
    |  | 3D 6D 7D TD QD  
    
    Flush with Diamonds
    
    |  | Player 2  If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.


    **4**|  | 4D 6S 9H QH QC  
    
    Pair of Queens  
    Highest card Nine
    
    |  | 3D 6D 7H QD QS  
    
    Pair of Queens  
    Highest card Seven
    
    |  | Player 1  
    **5**|  | 2H 2D 4C 4D 4S  
    
    Full House  
    With Three Fours
    
    |  | 3C 3D 3S 9S 9D  
    
    Full House  
    with Three Threes
    
    |  | Player 1  
      
    The file, [poker.txt](project/resources/p054_poker.txt), contains one-
    thousand random hands dealt to two players. Each line of the file contains
    ten cards (separated by a single space): the first five are Player 1's
    cards and the last five are Player 2's cards. You can assume that all
    hands are valid (no invalid characters or repeated cards), each player's
    hand is in no specific order, and in each hand there is a clear winner.
    
    How many hands does Player 1 win?
    
    """

    deals = parse_deals()
    identified = [(identify_hand(a), identify_hand(b)) for a, b in deals]
    wins = [(a, b)  for a, b in identified if player_one_wins(a, b)]

    if verbose > 0:
        for ident in identified:
            click.echo(format_deal(*ident))
            
    click.echo(len(wins))



Card = namedtuple('Card', 'rank suit')
Hand = namedtuple('Hand', 'name cards')

symbols = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}
ranks = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}


hand_order = {
    'highcard': 0,
    'pair': 1,
    '2pair': 2,
    '3ofakind': 3,
    'straight': 4,
    'flush': 5,
    'fullhouse': 6,
    '4ofakind': 7,
    'straightflush': 8,
    'royalflush': 9, 
}

def player_one_wins(hand_1, hand_2):

    return hand_order[hand_1.name] > hand_order[hand_2.name] or \
        (hand_order[hand_1.name] == hand_order[hand_2.name] and 
         tuple(c.rank for c in hand_1.cards) > tuple(c.rank for c in hand_2.cards))


def parse_deals():
    with Path('.', 'files', 'poker.txt').open('r') as f:
        for line in f:
            cards = [parse_card(c) for c in line.split(' ')]
            yield cards[:5], cards[5:]


def parse_card(card):
    return Card(parse_rank(card[0]), symbols.get(card[1]))


def parse_rank(rank):
    return int(ranks.get(rank, rank))


def get_ranks(hand):
    return {card.rank for card in hand}


def get_suits(hand):
    return {card.suit for card in hand}


def identify_hand(hand):
    ranks = Counter(c.rank for c in hand)
    suits = Counter(c.suit for c in hand)

    is_flush = len(suits) == 1
    straight_high = find_straight_high_card(set(ranks.keys()))

    if is_flush and straight_high == 14:
        return Hand('royalflush', sorted(hand, reverse=True))
    
    if is_flush and straight_high is not None:
        cards = tuple(sorted(hand, reverse=True))
        cards = cards[1:] + (cards[0], ) if straight_high == 5 else cards 
        return Hand('straightflush', cards)

    of_a_kind_rank, n_of_a_kind = ranks.most_common(1)[0]
    cards = sorted(hand, key=lambda c: (ranks[c.rank], c.rank), reverse=True)
    cards = tuple(cards)

    if n_of_a_kind == 4:
        return Hand('4ofakind', cards)

    if n_of_a_kind == 3 and len(ranks) == 2:
        return Hand('fullhouse', cards)

    if is_flush:
        return Hand('flush', cards)

    if straight_high is not None:
        cards = cards[1:] + (cards[0], ) if straight_high == 5 else cards 
        return Hand('straight', cards)

    if n_of_a_kind == 3:
        return Hand('3ofakind', cards)

    if n_of_a_kind == 2 and len(ranks) == 3:
        return Hand('2pair', cards)
    
    if n_of_a_kind == 2:
        return Hand('pair', cards)

    return Hand('highcard', cards)


def create_n_of_a_kind_hand(cards, name, rank):
    cards = [c for c in cards if c.rank == rank]
    others = [c for c in cards if c.rank != rank]
    return Hand(
        name,
        cards,
        (cards[0], ) + tuple(sorted(other)))
    

def find_straight_high_card(ranks):
    if len(ranks) != 5:
        return None

    if max(ranks) - min(ranks) == 4:
        return max(ranks)
    
    if ranks == {14, 2, 3, 4, 5}:
        return 5
    
    return None


def find_royal_flush(hand):
    return


def format_deal(hand1, hand2):
    return "{:<5} {} -- {}".format(str(player_one_wins(hand1, hand2)), format_hand(hand1), format_hand(hand2))


def format_hand(hand):
    return "{:>20} : {}".format(
        click.style(hand.name, bold=True),
        " ".join(format_card(c) for c in hand.cards))

def format_card(card):
    color = 'red' if card.suit in '♥♦' else 'black'
    rank = {10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(card.rank, card.rank)
    return click.style('{}{}'.format(rank, card.suit), fg=color, bg='white')