
"""
Solve the n-queens problem for a board of size N.

@param N - The size of the board.

@return A list containing the board representation of the solution.
"""
def n_queens(N): 
    #board is a NxN 2D list, created using a nested list comprehension. 
    #Each element of board is initialized to 0 meaning it holds no Queens 
    board = [[0 for x in range(N)] for x in range(N)] 
    solve_n_queens(board, 0, N, N) #indirect recursion #this is where the recursion and backtracking happens (ONLY IN THIS FUNCTION solve_n_queens)
    return board #final solution after use of helper methods

"""
Helper function to solve the n-queens problem recursively.

@param board - The current state of the board.
@param row - The current row we are trying to place a queen in.
@param N - The size of the board.
@param remaining - The number of queens yet to be placed.

@return True if a solution is found, False otherwise.

EX: N=3 board - Original (initial state) of N=3 board passed to solve_n_queens:
[
 [0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]
 ]

"""
def solve_n_queens(board, row, N, remaining):
# Base case
#STEP 1: Check if the number of remaining queens is zero, 
#       if so, return True indicating a solution has been found.
    if remaining == 0: #no remainings queens to place in cells (THERE IS NOTHING LEFT TO DO - WE DONE)
        return True    #return True since solution has been found

#STEP 2: Iterate over each column in the current row.
    for col in range(N): #iterating over the columns in current row 
#STEP 3: Check if the current cell is being attacked by any previously placed queen, 
#       using the is_attacked helper function.
        if is_attacked(row, col, board, N): #inderect recursion
#STEP 4: If the cell is attacked, continue to the next cell (this is bc it means we can't place the Queen in that cell)
            continue
        else:
#STEP 5: If the cell is not attacked, place a queen at the current cell by setting board[row][col] = 1.
            board[row][col] = 1 # Place the queen (1) & then move on to recursively solve for remaining queens
#STEP 6: Recursively call solve_n_queens w/ the updated board, the next row row+1, 
#       & w/ remaining-1 since we have placed a queen in this row.
         #we update the row, bc there can only be 1 queen per row
            if solve_n_queens(board, row+1, N, remaining-1): #direct recursion
#STEP 7: If the recursive call returns True, indicating a solution has been found, 
        #return True from the current call as well.
                return True
#STEP 8: If the recursive call returns False, indicating no solution was found, 
#       backtrack by removing the queen from the current cell by setting board[row][col] = 0.
            # Backtrack if any placement results in no solution
            board[row][col] = 0 #this is the where the backtracking is bc 1 represent a Queen, (each row can only contain a cell w one int 1, the rest of the cells must contain 0s)
    return False #if we didn't return true, we will return False after all no other option was left to do


"""
Check if row and col positions are valid for a queen placement.

@param row - The row position to check.
@param col - The column position to check.
@param board - The current state of the board.
@param N - The size of the board.

@return True if the position is under attack, False otherwise.



"is_attacked(row, col, board, N)" is a constraint checking function, 
which validates that no other queen is present in the row, column and in diagonal positions. 
"""
def is_attacked(row, col, board, N): #no recursive calls // called by solve_n_queens funciton
#ALL 3 FOR LOOPS WILL RUN TO CHECK ROW, COLUMN, AND NEGATIVE (\) & POSITIVE (/) DIAGONALS 

#------ Check row ------#
#STEP 1: for i in range(N) loop starts to check if the queen placed at (row, col) is attacked in its row.
    for i in range(N):
#STEP 2: Check if board[row][i] == 1. If true, a queen is already placed in the same row as (row, col), 
#        so return True indicating that the position is attacked.
        if board[row][i] == 1: #we check if each col in the row to see if any == 1 (indicating there is a queen there)
            return True
#STEP 3: If the loop completes without returning, move to the next loop.


#------ Check column ------#
#STEP 4: for i in range(N) loop starts to check if the queen placed at (row, col) is attacked in its column.
    for i in range(N):
#STEP 5: Check if board[i][col] == 1. If true, a queen is already placed in the same column as (row, col), so return True indicating that the position is attacked.
        if board[i][col] == 1:
            return True
#STEP 6: If the loop completes w/o returning, move to the next loop.


#------ Check diagonals ------#
#STEP 7: for i in range(N) & for j in range(N) loops start to check if the queen placed at (row, col) is attacked in its diagonal.
    for i in range(N):
        for j in range(N):
#STEP 8: Check if (i + j == row + col) or (i - j == row - col). If true, a queen is already placed in the same diagonal as (row, col), so return True indicating that the position is attacked.
            # In a chessboard, if the sum of the row & column indices of two cells are the same, 
            # then they lie on the same diagonal, i.e., the diagonal w/ slope +1. 
            # Similarly, if the difference between the row & column indices of two cells is the same, 
            # then they lie on the same diagonal, i.e., the diagonal w/ slope -1.
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return True
    return False


"""
Time complexity:
is_attacked - N loop + N loop + N*N loop


Space Complexity: 

-N*N board





Time Complexity:

The outer for loop executes for n times. 'is_attacked(row, col, board, N)' has a time complexity of O(n). 
The if condition where is_attacked() function is called would have a time complexity of O(n2). 

The recursive call is called n-1 times. 
Since it is in the for loop that is executed n times, it would have a running time of nT(n-1), if T(n) is the running time of the solve_n_Queens() function.

We can write the recurrence relation as 
T(n) = O(n^2) + nT(n-1)

Solving this recurrence relation would give the worst-case time complexity of O(n!).


This can be analyzed at a high level as, 
The first queen can be filled in n positions in the first row, 
the second queen in n-1 possible positions, 
the third queen in n-3 possible positions and so on. 

Resulting in time complexity of 

= O(n!)

"""