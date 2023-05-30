import sys #provides access to some variables used or maintained by the interpreter & to functions that interact strongly w/ the interpreter.

def makechange_topdown( coins, change):
    if change == 0: #base case
        return 0
    return makechange_topdown_helper(coins, change, [0] * (change + 1)) #[0] * (change + 1) creates a list of length change + 1 with all elements initialized to 0


def makechange_topdown_helper( coins, change, countmemo):

    """
countmemo = [0, 0, 0, 0, 0]

change = 3

if (change < 0):
    return -1
if (change == 0):
    return 0
if (countmemo[change] != 0):
    return countmemo[change]

In this example, change is set to 3 and countmemo is initialized w/ 5 elements, all set to 0.
The 1st if statement checks if change is less than 0. Since it's not (it's 3), it moves on to the next if statement.
The 2nd if statement checks if change is equal to 0. Since it's not (it's 3), it moves on to the third if statement.
The 3rd if statement checks if the value of countmemo at index change is not 0. Since countmemo[3] is indeed 0, this condition is not satisfied and the code continues on to the rest of the function.
"""
    if (change < 0):
        return -1
    if (change == 0):
        return 0
    if (countmemo[change] != 0):
        return countmemo[change]
    inf = sys.maxsize #sys.maxsize variable is used to set an initial value for inf and minimum_coins. sys.maxsize returns the largest positive integer that can be represented on a platform. By setting inf and minimum_coins to sys.maxsize, we are essentially initializing them to a value that is greater than any possible value they will take in the code.
    minimum_coins = sys.maxsize  # set to some maximum value

    for coin in coins: #iterates through each coin in the coins list.
        temp_coincount = makechange_topdown_helper(coins, change - coin, countmemo)

        if (temp_coincount >= 0 and temp_coincount < minimum_coins):
            minimum_coins = 1 + temp_coincount

    countmemo[change] = -1 if (minimum_coins == inf) else minimum_coins  # if we found a new minimum use it
    print(countmemo)
    print(len(countmemo))


    return countmemo[change]


print(makechange_topdown([5,3,1], 9))