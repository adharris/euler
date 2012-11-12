f = open('poker.txt')

ranks = {'T': 10, 'J':11, 'Q':12, 'K':13, 'A':14}



def card(c):
  r = c[0]
  if r in ranks:
    r = ranks[r]
  else:
    r = int(r)
  return (r, c[1]) 
  

def high_card(hand):
  q = max(hand)
  return q[0]

def one_pair(hand):
  for i in range(4):
    if hand[i][0] == hand[i+1][0]:
      return hand[i][0]
  return None

def two_pair(hand):
  one = one_pair(hand)  
  if one is None: return None
  for i in range(4):
    if hand[i][0] >= one: continue
    if hand[i][0] == hand[i+1][0]:
      return one * 100 + hand[i + 1][0]
  return None

def three_of_a_kind(hand):
  for i in range(3):
    if hand[i][0] == hand[i+1][0] and hand[i][0] == hand[i+2][0]:
      return hand[i][0]
  return None

def straight(hand):
  last = hand[0][0]
  for i in range(1, 5):
    if hand[i][0] != last - 1:
      return None
    last = hand[i][0]
  return hand[0][0]

def flush(hand):
  suit = hand[0][1]
  for i in range(1, 5):
    if hand[i][1] != suit:
      return None
  return hand[0][0]

def full_house(hand):
  if hand[0][0] != hand[1][0]: return None
  if hand[3][0] != hand[4][0]: return None
  if hand[2][0] != hand[0][0] and hand[2][0] != hand[4][0]: return None
  if hand[2][0] == hand[0][0]:
    return hand[2][0] * 100 + hand[4][0]
  else:
    return hand[2][0] * 100 + hand[0][0]
  
def four_of_a_kind(hand):
  for i in range(2):
    if hand[i][0] == hand[i+1][0] and hand[i][0] == hand[i+2][0] and hand[i][0] == hand[i+3][0]:
      return hand[i][0]
  return None

def straight_flush(hand):
  st = straight(hand)
  fl = flush(hand)
  if st is None or fl is None:
    return None
  return hand[0][0]

hands = [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, one_pair, high_card]

def compare_hands(h1, h2):
  r1 = get_hand(h1)
  r2 = get_hand(h2)
  
  if r1[0] < r2[0]: return True
  if r1[0] > r2[0]: return False

  #same hand
  if r1[1] > r2[1]: return True
  if r1[1] < r2[1]: return False
  
  if h1[0][0] > h2[0][0]: return True
  return False

def get_hand(hand):
  h = [h(hand) for h in hands]
  for i in range(len(h)):
    if not h[i] is None:
      return (i, h[i])

count = 0
for row in f:
  r = row.split()
  p1 = sorted(map(lambda x: card(x), r[:5]), reverse=True)
  p2 = sorted(map(lambda x: card(x), r[5:]), reverse=True)
  if compare_hands(p1, p2):
    count += 1

print count


