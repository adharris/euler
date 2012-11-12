coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

def coin_count(total_left, coin):
  coin_amount = coins[coin]
  count = 0
  coin_c= 0
  while coin_c* coin_amount <= total_left:
    if coin_c* coin_amount == total_left:
      count += 1
    elif coin < len(coins) - 1:
      count += coin_count( total_left - coin_c* coin_amount, coin + 1)
    coin_c+= 1

  return count

print coin_count(target, 0)
