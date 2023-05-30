"""
You are a pet store owner and you own few dogs.
 Each dog has a specific hunger level given by array hunger_level [1..n] 
 (ith dog has hunger level of hunger_level [i]). 
 
You have couple of dog biscuits of size given by biscuit_size [1…m]. 
Your goal to satisfy maximum number of hungry dogs. 

You need to find the number of dogs we can satisfy.
If a dog has hunger hunger_level[i], it can be satisfied only by taking a biscuit of size biscuit_size [j] >= hunger_level [i] 
(i.e biscuit size should be greater than or equal to hunger level to satisfy a dog.)
If no dog can be satisfied return 0.

Conditions:
You cannot give same biscuit to two dogs.
Each dog can get only one biscuit.


Example 1:
Input: hunger_level[1,2,3], biscuit_size[1,1]
Output: 1
Explanation: Only one dog with hunger level of 1 can be satisfied with one cookie of size 1.

Example 2:
Input: hunger_level[2, 1], biscuit_size[1,3,2]
Output: 2
Explanation: Two dogs can be satisfied. The biscuit sizes are big enough to satisfy the hunger level of both the dogs.


a. Describe a greedy algorithm to solve this problem (write documentation)

b. Write an algorithm implementing the approach. 
    Your function signature should be feedDog(hunger_level, biscuit_size); hunger_level, 
    biscuit_size both are one dimention arrays . Name your file FeedDog.py

c. Analyse the time complexity of the approach. (Say what the time complexity is and why)




"""

"""
@param hunger_level - list of containing of level of hunger  of dog[i] at index i
@param biscuit_size - list of containing of biscuit sizes, each element represents 1 buscuit 

@return happyDogs - number of dogs we are able to satisfy hunger of

hunger_level = [1]
biscuit_size = [4]


Time Complexity:
Why: 

"""
def feedDog(hunger_level,biscuit_size):
	#would this be considered a greedy algorithm if arrays are not sorter
	hunger_level.sort()  #O(nlogn)  #n-size
	biscuit_size.sort() #O(mlogm) #m-size
	
	happyDogs =0
	j=0 #pointer to iterate through the hunger_level array
	
	for biscuit_i in biscuit_size:
		for k in range(j,len(hunger_level)):
			if(biscuit_i >= hunger_level[k]):
				happyDogs+=1
				j=j+1
				break
		if(j==len(hunger_level)):
			return happyDogs
			
	return happyDogs






