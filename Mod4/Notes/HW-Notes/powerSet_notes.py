

"""
*  Recursive helper function for generating the power set of a given input set using backtracking.

* @param: pointer -  the index of the current element being considered
* @param: choices_made -  the list of choices made so far in generating the power set
* @param: inputSet - the input set for which the power set needs to be generated
* @param: result - the list of all possible subsets of the input set, including the empty set

* @return:


"""

def powerset_helper(pointer, choices_made, inputSet, result):
    if pointer < 0: #BASE CASE - If it is, then we have reached the end of the input set & so
        #we append a shallow copy of the choices made so far to the result list and return.
        result.append(choices_made.copy()) #appending to result list (argument passed (in Python arguments are always passed as reference) )
        return # returning control to the caller function; not returning any value.
    

    """The base case in the recursive algorithm is when the pointer variable becomes less than 0. 
    This means that all the elements of the inputSet have been either included or excluded from the choices_made list, 
    & thus we have generated a valid subset. 
    At this point, we append a copy of the choices_made list to the result list & return."""

    choices_made.append(inputSet[pointer]) 
    powerset_helper(pointer - 1, choices_made, inputSet, result) #direct recursion

    choices_made.pop() 
    """ The backtracking is happening when we remove the last item from the choices_made list using choices_made.pop(). 
    By doing this, we undo the last choice we made and backtrack to the previous state, which allows us to explore other possible choices. 
    This process is repeated recursively until all possible subsets have been explored."""
    powerset_helper(pointer - 1, choices_made, inputSet, result) #direct recursion



"""
 * Generates the power set of a given input set using backtracking.

 * @param: inputSet -  the input set for which the power set needs to be generated

 * @return: result - a list of all possible subsets of the input set, including the empty set
"""



""" The result parameter is initially an empty list that is passed to the powerset_helper function. 
The function fills the result list with all the subsets of the inputSet. 
Once all the recursive calls are finished, the result list will contain all the subsets of the inputSet.

This is because in the powerset_helper function, every time a valid subset is found, i.e., pointer < 0, a copy of the choices_made list is appended to the result list.
 At the end of the powerset function, the filled result list is returned.
"""

def powerset(inputSet):
    result = []
    powerset_helper(len(inputSet) - 1, [], inputSet, result)
    return result


"""
result - 


The 'result' list is a multidimensional list in the powerset function. 
Each element of the list represents a subset of the input set, 
 - & the list contains all possible subsets of the input set, 
- including the empty set.

"""
