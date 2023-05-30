"""Given two DNA strings find the length of the longest common string alignment between them 
(it need not be continuous). 
Assume empty string does not match with anything"""


"""
a.	Implement a solution to this problem using Top-down Approach of Dynamic Programming, 
name your function dna_match_topdown(DNA1, DNA2):
"""

def dna_match_topdown(DNA1, DNA2):
    # initialize cache
    cache = [[-1 for j in range(len(DNA2))] for i in range(len(DNA1))] #only filling up cells of cache we need
    # call recursive helper function
    return lcs_topdown(DNA1, DNA2, len(DNA1)-1, len(DNA2)-1, cache)

def lcs_topdown(DNA1, DNA2, i, j, cache):
    # base case: one of the strings is empty
    if i < 0 or j < 0:
        return 0
    # check if already computed and return value from cache
    if cache[i][j] != -1:
        return cache[i][j]
    # if last characters match, add 1 to LCS and recur for remaining strings
    if DNA1[i] == DNA2[j]:
        cache[i][j] = 1 + lcs_topdown(DNA1, DNA2, i-1, j-1, cache)
    else:
        # find LCS by excluding last character of DNA1 and last character of DNA2
        # take maximum of two possible ways
        cache[i][j] = max(lcs_topdown(DNA1, DNA2, i-1, j, cache), lcs_topdown(DNA1, DNA2, i, j-1, cache))
    return cache[i][j]


"""
b.	Implement a solution to this problem using Bottom-up Approach of Dynamic Programming, 
name your function dna_match_bottomup(DNA1, DNA2) 
Write implementation of a & b in a single python file, name your file DNAMatch.py 
Do not write the functions in a Python class.
"""
def dna_match_bottomup(DNA1, DNA2):
    # initialize cache
    cache = [[0 for j in range(len(DNA2)+1)] for i in range(len(DNA1)+1)] #filling up all cells of cache
    # fill cache bottom-up
    for i in range(1, len(DNA1)+1):
        for j in range(1, len(DNA2)+1):
            if i == 0 or j==0:
                cache[i][j] = 0
            elif DNA1[i-1] == DNA2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    # return length of LCS
    return cache[len(DNA1)][len(DNA2)]

