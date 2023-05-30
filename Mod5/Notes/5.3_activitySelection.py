
"""
    The activity_selection function returns a single list of activities, 
    representing the most optimal solution based on the given conditions. 
    It selects activities one by one, considering their start times and end times, 
    and adds them to the result list if they meet the condition (start_times[i] >= blocked_time).

    Since it chooses activities in a greedy manner, it aims to maximize the number of activities selected 
    while ensuring non-overlapping time intervals. Therefore, the returned result list represents the optimal 
    solution that maximizes the number of activities without any time conflicts.

    In summary:
    Selects a maximum set of mutually compatible activities based on their start and end times.

    Parameters:
        @param activities (1D list) -  List of activity names.
        @param start_times (1D list) - List of activity start times.
        @param end_times (1D list) - List of activity end times.

    Returns:
        @return result (1D list) - List containing the selected activities.

    Example:
        >>> activity_selection(['A', 'B', 'C', 'D', 'E'], [1, 3, 0, 5, 8], [2, 4, 6, 7, 9])
        ['A', 'B', 'D']
    
    PS: Assume that the activities are passed in the ascending order of their ending times, 
        so you don't have to sort them.

"""
def activity_selection(activities, start_times, end_times):
    result = []
    blocked_time = 0 #represents the end time of the last selected activity


    # The reason for starting from 1 instead of 0 is to compare the start time of each activity 
    # w the end time of the previously selected activity, which is represented by blocked_time.

    #activities[i] - activity in list activities at index i
    for i in range(1, len(activities)): #By starting from 1, we skip the 1st activity bc there's no previously selected activity to compare its start time w.
        #If the start time of the current activity is greater than or equal to the blocked time, 
        # it means that there is no overlap between the current activity and the previously selected activity. 
        # In this case, we can add the current activity to the result list.
        if start_times[i] >= blocked_time: 
            result.append(activities[i])
            #update the "blocked_time" w the end time of the chosen activity 
            # so that we can pick our next activity that starts immediately after the "blocked_time".
            blocked_time = end_times[i] 
    return result



"""
    Time Complexity: The running time of our solution will be O(n). 
    Space complexity will be O(n).

    If the ending times are not sorted, 
    what will be the best time complexity to solve the activity selection problem 
    using the same technique that we discussed above?

    O(n logn)
    Explanation: we will have to spend additional time in sorting the array of size n. 
    The best running time sorting algorithm - merge sort would take nlogn time.
"""

""" 
The part that makes this a greedy algorithm is the selection of activities based on a greedy criterion. 
The algorithm iterates over the activities and, at each step, selects the activity that has a start time 
greater than or equal to the current blocked time.

By choosing the activity w the earliest start time that is compatible with the previous selections 
(i.e., its start time is greater than or equal to the blocked time), the algorithm prioritizes activities 
that can be performed w/o overlapping w the previous ones.

This greedy selection criterion aims to maximize the number of activities that can be scheduled within the given time frame. 
The algorithm does not consider the future consequences of its decisions or explore all 
possible combinations of activities. Instead, it makes locally optimal choices at each step, 
assuming they will lead to a globally optimal solution.

The greedy nature of the algorithm lies in the fact that it makes immediate decisions based solely on the current state, 
w/o reconsidering or backtracking.
"""