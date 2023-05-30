def amount(A, S):
    result = [] #c
    backtrack(A, S, [], result) #O(n)
    return result 

def backtrack(A, target, combination, result):
    if target == 0:
        result.append(combination[:])  # Add a copy of the combination to the result
        return
    if target < 0:
        return
    
    for i in range(len(A)):
        combination.append(A[i])
        backtrack(A[i + 1:], target - A[i], combination, result) #T(n-1) + T #RECURSIVE STEP
        combination.pop()  #backtrack


print(amount([7, 1, 6, 2, 5,], 7))
# print(amount([1, 6, 2, 5, 7], 7))
# print(amount([1, 1, 2, 2, 3, 4, 5, 7], 7))

#recurrence relation: T(n) = T(n-1) + T(n-2) + T(n-3) + ... + T(1) + O(1)

"""
The recurrence relation for the given algorithm can be expressed as follows:

T(n) = T(n-1) + T(n-2) + T(n-3) + ... + T(1) + O(1)

This recurrence relation represents the time complexity of the algorithm in terms of the input size n. 
It states that the time needed to solve a problem of size n is equal to the sum of the times needed to solve subproblems of smaller sizes (n-1, n-2, n-3, ..., 1), 
plus the constant time operations performed within each recursive call.

In this case, each recursive call in the backtrack function corresponds to solving a subproblem of size n-1, as the list A is reduced by one element in each call. 
Therefore, the recurrence relation represents the recursive nature of the algorithm,
where the time needed to solve a problem of size n depends on the times needed to solve smaller subproblems.

It's important to note that the recurrence relation assumes that the constant time operations performed within each recursive call can be ignored in the analysis, 
as their contribution becomes negligible compared to the recursive calls as the input size grows.

"""