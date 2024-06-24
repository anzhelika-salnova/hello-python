"""
There are coins on the table. Some of them are heads up, and others are tails up. 
Determine the minimum number of coins need to be turned over, 
so that all the coins lie with the same side up.

Data-in: 
coins[i] = 0 - i-coin is head up 
coins[i] = 1 - i-coin is tail up 

Data-out: 
One integer - the minimum number of coins need to be turned over.
"""

coins = [1, 0, 0, 1, 0, 0, 1, 0]

head = 0
tail = 0 

for coin in coins:
    if coin == 1:
        head +=1 
    else:
        tail +=1

print(min(head, tail))

