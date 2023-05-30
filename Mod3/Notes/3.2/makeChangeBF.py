"""
    @returns the minimum number of coins needed to make the specified change using a brute-force algorithm.

    @param:
        1. coins (list of int): A list of coin denominations available for making change.
        2. change (int): The amount of change to make.

    Returns:
        minCoins (int): The minimum number of coins needed to make the specified change. 
        If it is not possible to make the change, the function returns an arbitrary large number (which in this implementation is `change + 1`). 
"""



def makechangeBF(coins, change):
    if(change == 0): return 0
    minCoins = change+1 #some arbitary huge number that cannot be the answer

    for i in range(len(coins)):
        if(coins[i] <= change):
            minCoins = min(minCoins, makechangeBF(coins, change-coins[i]) + 1) #ex: result = min(10, makeChangeBF(3, 9-1) - ) = result = min(10, makeChangeBF(3, 8))
    return minCoins

print(makechangeBF([1,3,5] , 9 ))