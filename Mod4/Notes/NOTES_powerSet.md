**EXAMPLE**


Let's say our input set is **inputSet = [1, 2, 3]** and we want to compute its power set using the **powerset()**  function.

Initially, the result list is empty. The function starts by calling powerset_helper(len(inputSet) - 1, [], inputSet, result).

    pointer is initially 2, since len(inputSet) - 1 is 2.
    choices_made is initially an empty list [], since we haven't made any choices yet.
    inputSet is [1, 2, 3], our input set.
    result is initially an empty list [].

Then, we call the powerset_helper function recursively:

    On the first recursive call, we add the last element of inputSet (i.e., 3) to choices_made by calling choices_made.append(inputSet[pointer]). choices_made now contains [3].
    We then call powerset_helper again with pointer - 1 (i.e., 1), choices_made, inputSet, and result.
    This time, on the first recursive call, we add the second-to-last element of inputSet (i.e., 2) to choices_made by calling choices_made.append(inputSet[pointer]). choices_made now contains [3, 2].
    We then call powerset_helper again with pointer - 1 (i.e., 0), choices_made, inputSet, and result.
    On the third recursive call, we add the first element of inputSet (i.e., 1) to choices_made by calling choices_made.append(inputSet[pointer]). choices_made now contains [3, 2, 1].
    We then append a deep copy of choices_made (i.e., [3, 2, 1]) to result by calling result.append(choices_made.copy()). result now contains [[3, 2, 1]].
    We return from this call.
    On the fourth recursive call, we remove the last element from choices_made by calling choices_made.pop(). choices_made now contains [3, 2].
    We then call powerset_helper again with pointer - 1 (i.e., 0), choices_made, inputSet, and result.
    On the fifth recursive call, we add the first element of inputSet (i.e., 1) to choices_made by calling choices_made.append(inputSet[pointer]). choices_made now contains [3, 1].
    We then append a deep copy of choices_made (i.e., [3, 1]) to result by calling result.append(choices_made.copy()). result now contains [[3, 2, 1], [3, 1]].
    We return from this call.
    On the sixth recursive call, we remove the last element from choices_made by calling choices_made.pop(). choices_made now contains [3].
    We then call powerset_helper again with pointer - 1 (i.e., 1), choices_made, inputSet, and result.
    On the seventh recursive call, we add