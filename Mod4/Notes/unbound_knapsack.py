


# W (the maximum weight capacity)
#n (the number of items)
# weights (a list of item weights)
# values (a list of item values).

def unbound_knapsack(W, n, weights, values): 
    dp = [0]*(W+1) #list will be used to store the maximum possible value that can be obtained for each possible weight

    for x in range(1, W+1): #x represents each index(weight) from 1 up to capacity W
        for i in range(n):
            wi = weights[i]
            if wi <= x: #if wi at index i in list weight <= sub capacity x
                dp[x] = max(dp[x] , dp[x-wi] + values[i]) #take max of current value in dp[x] or if there is a higher value to be added 

    return dp[W]
print(unbound_knapsack(10,5,[4,9,3,5,7], [10,25,13,20,8]))

def unbound_knapsack2(CAP_W, n, weights, values): 
    cache = [0]*(CAP_W+1) #list will be used to store the maximum possible value that can be obtained for each possible weight

    for subCap_w in range(1, CAP_W+1): #x represents each index(weight) from 1 up to capacity W
        for i in range(n):
            wi = weights[i]
            if wi <= subCap_w: #if wi at index i in list weight <= sub capacity x
                cache[subCap_w] = max(cache[subCap_w] , cache[subCap_w-wi] + values[i]) #take max of current value in dp[x] or if there is a higher value to be added 

    return cache[CAP_W]
print(unbound_knapsack2(10,5,[4,9,3,5,7], [10,25,13,20,8]))