

from copy import deepcopy

"""
@param nums - order list of positive integers from which we will make combinations of numbers that make up the sum target
@param start - the index to start considering elements from nums
@param result - initally an empty list to which we will append lists of combinations of nubmers that sum up to target
@param remainder - the number that we still have to sum up to (target - the amoutns that have already been added) - this is intially passed as value held by variable target
@param combination - list that we will update to hold 

@return
"""

def combination_sum_helper(nums, start, result, remainder, combination):
#BASE CASE - 1    
#STEP 1: we check if there is anything remaining to find a combination for     
    if(remainder == 0): #we have summed up to target value, target has no amount remaining to sum to it
        #the current combination is added to the result list (after making a deep copy of the combination to avoid reference issues), & the function returns.
        result.append(deepcopy(combination)) 
        return #return control to caller function

#STEP 2:If remainder is negative, it means the sum has exceeded the target. 
# In this case, the function returns w/o taking any further action.
#BASE CASE - 2    
    elif( remainder <0):
        return # sum exceeded the target
    
#STEP 3: 
#If neither of the above conditions is met, the function enters a loop that starts from the start index & iterates thru the nums list.
#STEP 4:
#In each iteration of the loop, the current element from nums is appended to the combination list.
    for i in range(start, len(nums)):
        combination.append(nums[i]) #append element to combinations list

#STEP 5: The combination_sum_helper function is recursively called w/ the updated remainder (subtracting the current element) & the updated combination.
        combination_sum_helper(nums, i, result, remainder-nums[i], combination)

#STEP 6: After the recursive call returns , the function reaches the backtrack step, where the last element added to the combination list is removed using the combination.pop() method.
        #backtrack
        combination.pop() #backtrack to previous value

#STEP 7: The loop continues to the next iteration, trying the next element from nums.

#Once the combination_sum_helper function completes all iterations & backtracks as necessary, 
# the result list in the combination_sum function contains all the valid combinations that sum up to the target.


"""

@param num - order list of positive integers from which we will make combinations of numbers that make up the sum target
@param target - the sum we want to make from different possible combinations of the numbers contained in the nums[] list

@print result - the final version of result; a list of lists containing all possible combinations that sum of to the target value
"""
def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[]) #helper funciton where recursion & backtracking happens
    print(result)

print(combination_sum([2,3,6,7], 7 ))


