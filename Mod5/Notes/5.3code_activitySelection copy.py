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

