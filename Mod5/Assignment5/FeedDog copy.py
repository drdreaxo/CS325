def feedDog(hunger_level, biscuit_size):
    hunger_level.sort() #O(nlogn)
    biscuit_size.sort() #O(nlogn)
    happyDogs = 0

    for i in hunger_level:
        if len(biscuit_size) == 0:
            break
        if i in biscuit_size:
            biscuit_size.remove(i)
            happyDogs += 1
    return happyDogs



print(feedDog([1,2,3],[1,1] ))
print(feedDog([2, 1],[1,3,2] ))
print(feedDog([1, 2, 3],[3, 2, 1]))

"""

   
For sorting array time complexity will be nlogn + mlogm where n and m is the length of both array

And for mapping biscuit and hunger dog, it will take m+n where n and m is the length of both array

So time complexity will be nlogn + mlogm + m + n

So Time complexity will be O(N log N) in bigO notation, where N is max( len( hunger_index) , len( biscuit_size) ) 
"""



# def feedDog(hunger_level, biscuit_size):
#     happyDogs = 0
#     biscuits = {}
#     for size in biscuit_size:
#         if size in biscuits:
#             biscuits[size] += 1
#         else:
#             biscuits[size] = 1
#     for hunger in hunger_level:
#         if hunger in biscuits and biscuits[hunger] > 0:
#             biscuits[hunger] -= 1
#             happyDogs += 1
#     return happyDogs



# print(feedDog2([1,2,3],[1,1] ))
# print(feedDog2([2, 1],[1,3,2] ))






"""

Ex 1:
Input: hunger_level[1,2,3], biscuit_size[1,1]
Output: 1
Explanation: Only one dog with hunger level of 1 can be satisfied with one cookie of size 1.

Ex 2:
Input: hunger_level[2, 1], biscuit_size[1,3,2]
Output: 2
Explanation: Two dogs can be satisfied. The biscuit sizes are big enough to satisfy the hunger level of both the dogs."""