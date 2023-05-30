"""
You are given a 3-D puzzle. 
The length & breadth of the puzzle is given by a 2D matrix puzzle[m][n]. 
The height of each cell is given by the value of each cell, the value of puzzle[row][column] give the height of the cell [row][column]. 
You are at [0][0] cell and you want to reach to the bottom right cell [m-1][n-1], the destination cell. You can move either up, down, left, or right. 

Write an algorithm to reach the destination cell with minimal effort.
How effort is defined: The effort of route is the maximum absolute difference between two consecutive cells.
If a route requires us to cross heights: 1, 3, 4, 6, 3, 1
The absolute differences between consecutive cells is: |1-3| = 2, |3-4|=1, |4-6|=2, |6-3|=3, |3-1|=2; this gives us the values: {2, 1, 2, 3, 2}. 
The maximum value of these absolute differences is 3. 
Hence the effort required on this path will be: 3.

Example:
Input: puzzle[][] = [[1, 3, 5], [2, 8, 3], [3, 4, 5]] 

Output: 1
Explanation: 
The minimal effort route would be [1, 2, 3, 4, 5] which has an effort of value 1. 
This is better than other routes for instance, route [1, 3, 5, 3, 5] which has an effort of 2.
"""

"""To represent the 3-D puzzle in a 2D matrix, 
each cell of the matrix corresponds to a specific position in the puzzle. 
The value in each cell of the matrix represents the height of the corresponding cell in the puzzle.
"""






""" Finds the minimum effort required to traverse a puzzle grid.

    @param - puzzle (list[list[int]]): A 2D matrix representing the puzzle grid. Each element represents the height of the corresponding cell.

    @returns - efforts (int): The minimum effort required to traverse the entire puzzle grid.
"""

def minEffort(puzzle):
    m = len(puzzle)  # Number of rows
    n = len(puzzle[0])  # Number of columns


    efforts = [[float('inf')] * n for _ in range(m)] #2D array to store the efforts/costs associated w/ each cell in the puzzle.
    efforts[0][0] = 0  #Effort of starting cell is 0 #signifies that there's no additional effort required to move from the starting cell to itself.

    #Create a queue for BFS traversal
    queue = [(0, 0)] # breadth-first manner, meaning it visits all the neighbors of a vertex before moving on to the next level of neighbors.
    #We assume the presence of a cell at position (0, 0) as the starting point of the traversal.
    #(0, 0) represents the coordinates of the starting cell in the puzzle.

    # Define the possible directions to move
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # (1, 0): Move down by 1 row.
    # (-1, 0): Move up by 1 row.
    # (0, 1): Move right by 1 column.
    # (0, -1): Move left by 1 column.

    while queue:
        row, col = queue.pop(0)

        # Explore all possible directions
        for drow, dcol in directions:
            new_row, new_col = row + drow, col + dcol

            # Check if the new position is within the puzzle boundaries
            if 0 <= new_row < m and 0 <= new_col < n:
                # Calculate the effort for the new position
                new_effort = max(efforts[row][col], abs(puzzle[new_row][new_col] - puzzle[row][col]))

                # Update the effort if it's smaller than the previous value
                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    queue.append((new_row, new_col))

    return efforts[m - 1][n - 1]
