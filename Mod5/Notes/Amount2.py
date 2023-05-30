def amount(A, S):
    result = []
    backtrack(A, S, [], result)
    return result

def backtrack(A, target, combination, result):
    if target == 0:
        result.append(combination[:])  # Add a copy of the combination to the result
        return
    if target < 0:
        return
    
    for i in range(len(A)):
        if i > 0 and A[i] == A[i-1]:
            continue  # Skip duplicates to avoid duplicate combinations
        combination.append(A[i])
        backtrack(A[i + 1:], target - A[i], combination, result)
        combination.pop()  # Remove the last element to backtrack

A = [7, 1, 6, 2, 5]
S = 7
result = amount(A, S)
print(result)



print(amount([7, 1, 6, 2, 5,], 7))
print(amount([1, 6, 2, 5, 7], 7))
print(amount([1, 1, 2, 2, 3, 4, 6, 2, 5, 7], 7))