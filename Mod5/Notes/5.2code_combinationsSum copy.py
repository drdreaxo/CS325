def amount(A, S):
    result = []

    backtrack(A, S, [], result, 0) #

    return result

def backtrack(A, target, combination, result, start):
    if target == 0:
        result.append(combination[:])
        return
    if target <0:
        return # sum exceeded the target
    
    for i in range(start, len(A)):
        combination.append(A[i]) #combination

        #  backtrack([7, 1, 6, 2, 5,], 0, [7], [[7]], 0)
        backtrack(A, target - A[i], combination, result, i)
        combination.pop()  #backtrack

print(amount([7, 1, 6, 2, 5,], 7))
# print(amount([1, 6, 2, 5, 7], 7))
# print(amount([1, 1, 2, 2, 3, 4, 6, 2, 5, 7], 7))