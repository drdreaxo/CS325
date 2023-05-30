# """
#     @returns the minimum number of coins needed to make the specified change using a brute-force algorithm.

#     @param:
#         1. coins (list of int): A list of coin denominations available for making change.
#         2. change (int): The amount of change to make.

#     Returns:
#         minCoins (int): The minimum number of coins needed to make the specified change. 
#         If it is not possible to make the change, the function returns an arbitrary large number (which in this implementation is `change + 1`). 
# """



# def makechangeBF(coins, change, changeMemo = {}):
#     changeMemo = {0:0, 1:1}
#     if(change == 0): return 0
#     minCoins = change+1 #some arbitary huge number that cannot be the answer

#     if change in changeMemo:
#         return changeMemo[change]
    
#     for i in range(len(coins)):
#         if(coins[i] <= change):
#             minCoins = min(minCoins, makechangeBF(coins, change-coins[i]) + 1) #ex: result = min(10, makeChangeBF(3, 9-1) - ) = result = min(10, makeChangeBF(3, 8))
    
#     changeMemo[change] = minCoins
#     return minCoins
# print(makechangeBF([1,3,5] , 9 ))



# def makeChange2(coins, change, changeMemo={}):
#     if(change == 0): return 0
#     minCoins = change+1 #some arbitrary huge number that cannot be the answer
#     if change in changeMemo:
#         return changeMemo[change]
#     for i in range(len(coins)):
#         if(coins[i] <= change):
#             minCoins = min(minCoins, makeChange2(coins, change-coins[i], changeMemo) + 1)
#     changeMemo[change] = minCoins
#     return minCoins
# print(makeChange2([1,3,5], 9))




# def makechangeBF(coins, change):
#     changeMemo = {} #{changeLeft, coinsTakenForThatChange}
#     if change == 0: return 0
#     elif change ==1: return 1
#     minCoins = change+1 #some arbitrary huge number that cannot be the answer

#     if change in changeMemo:
#         return changeMemo[change]
#     else:
#         for i in range(len(coins)):
#             if(coins[i] <= change):
#                 remainingChange = change-coins[i]
#                 minCoins = min(minCoins, makechangeBF(coins, remainingChange) + 1) #ex: result = min(10, makeChangeBF(3, 9-1) - ) = result = min(10, makeChangeBF(3, 8))
#                 changeMemo[remainingChange] = minCoins

#     print(changeMemo)
#     return minCoins

# print(makechangeBF([1,3,5] , 9 ))



def makechangeBF(coins, change, changeMemo):
    if change == 0:
        return 0
    elif change == 1:
        return 1
    elif change in changeMemo:
        return changeMemo[change]
    else:
        minCoins = change + 1
        for coin in coins:
            if coin <= change:
                remainingChange = change - coin
                coinsForRemainingChange = makechangeBF(coins, remainingChange, changeMemo) + 1
                if coinsForRemainingChange < minCoins:
                    minCoins = coinsForRemainingChange
                    changeMemo[change] = minCoins
        return minCoins
    

changeMemo = {}
print(makechangeBF([1, 3, 5], 9, changeMemo))
print(changeMemo)

