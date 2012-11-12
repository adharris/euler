from random import shuffle, randint

def roll():
  return (randint(1, 4), randint(1, 4))

class Deck:
  def __init__(self, cards):
    self.cards = cards
    self.index = 0
    self.shuffle()
  def shuffle(self):
    shuffle(self.cards)
  def get_card(self):
    self.index = (self.index + 1) % len(self.cards)
    return self.cards[self.index]
  def __str__(self):
    return str(self.cards)

class Board:
  player = 0
  counts = [0]*40
  turn_count = 0
  double_count = 0
  squares = ['GO', 'A1', 'CHEST1', 'A2', 'T1', 'RAIL1', 'B1', 'CHANCE1', 'B2', 'B3',
             'JAIL', 'C1', 'UTIL1', 'C2', 'C3', 'RAIL2', 'D1', 'CHEST2', 'D2', 'D3',
             'FP', 'E1', 'CHANCE2', 'E2', 'E3', 'RAIL3', 'F1', 'F2', 'UTIL2', 'F3',
             'GTJ', 'G1', 'G2', 'CHEST3', 'G3', 'RAIL4', 'CHANCE3', 'H1', 'T2', 'H2']
  
  def draw_chest(board):
    card = board.chest.get_card()
    return card(board)

  def draw_chance(board):
    card = board.chance.get_card()
    return card(board)

  def next_of(self, list):
    i = board.player
    while True:
      i += 1
      i %= len(board.squares)
      if i in list:
        return i

  board_actions = {
      30: lambda pos: 10,
      2:  draw_chest,
      17: draw_chest,
      33: draw_chest,
      7: draw_chance,
      22: draw_chance,
      36: draw_chance,
      }
  chest  = Deck([
    lambda board: 10,
    lambda board: 0,
    ] + [lambda board: board.player] * 14)
  chance = Deck([
    lambda board: 0, # Advance to go
    lambda board: 10, # Go to jail
    lambda board: 11, # Go to C1
    lambda board: 24, # Go to E3
    lambda board: 39, # Go to H2
    lambda board: 5, # Go to first rail
    lambda board: board.next_of((5, 15, 25, 35)),
    lambda board: board.next_of((5, 15, 25, 35)),
    lambda board: board.next_of((12, 28)),
    lambda board: (board.player - 3) % len(board.squares), # go back 3
    ] +  [lambda board: board.player] * 6 )

  def turn(self):
    r = roll()

    self.player += sum(r)
    self.player %= len(self.squares)

    # Three doubles
    if r[0] == r[1]: 
      self.double_count += 1
    if self.double_count == 3:
      self.player = 10

    #Actions
    while True:
      if self.player in self.board_actions:
        p = self.player
        p2 = self.board_actions[self.player](self)
        if p == p2:
          break
        self.player = p2
      else:
        break

    if self.player == 10: 
      self.double_count = 0

    self.turn_count += 1
    self.counts[self.player] += 1

  def __str__(self):
    s = sorted({(float(self.counts[key]) / self.turn_count, key) for key in range(len(self.counts))}, reverse=True)
    st = ''
    for i in range(len(s)):
      st += '%7s: %.2f%% (Position %02d, Visits: %d)\n' % (self.squares[s[i][1]], s[i][0] * 100, s[i][1], self.counts[s[i][1]])
    return st


board = Board()
for i in range(10000000):
  board.turn()
  if i % 100000 == 0: print i
print board
