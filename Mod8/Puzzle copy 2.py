"""

@INSTRUCTIONS:
    You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be different). 
    Each cell in the puzzle is either empty or has a barrier. 
    An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. 
    You are given two coordinates from the puzzle (a,b) and (x,y). 
    You are currently located at (a,b) and want to reach (x,y). 
    You can move only in the following directions.

    L: move to left cell from the current cell
    R: move to right cell from the current cell
    U: move to upper cell from the current cell
    D: move to the lower cell from the current cell

    You can move to only an empty cell & cannot move to a cell with a barrier in it. 
    Your goal is to reach the destination

    Input: board, source, destination.
    Puzzle: A list of lists, each list represents a row in the rectangular puzzle. 
            Each element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable). 
            The same as in the example.
    source: A tuple representing the indices of the starting position, e.g. for the upper right corner, source=(0, 4).
    destination: A tuple representing the indices of the goal position, e.g. for the lower right corner, goal=(4, 4).

    Output: A list of tuples representing the indices of each position in the path. 
            The first tuple should be the starting position, or source, and the last tuple should be the destination. 
            If there is no valid path, None should be returned. 
            Not an empty list, but the None object.

    Note: The order of these tuples matters, as they encode a path. 
        Each position in the path must be empty (correspond to a ‘-’ on the board) & adjacent to the previous position.

    Example 1 (consider above puzzle)
    Input: puzzle, (0,2), (2,2)
    Output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
    Example 2 (consider above puzzle)
    Input: puzzle, (0,0), (4,4)
    Output: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    Example 3: (consider above puzzle)
    Input: puzzle, (0,0),
"""



"""
Solves a 2-D puzzle to find the path from source to destination.

@param - board (List[List[str]]): A 2-D puzzle represented as a list of lists, where each inner list represents a row.
        Each element can be '-' for an empty cell or '#' for a barrier cell.
@param - source (Tuple[int, int]): The starting position represented as a tuple of row and column indices.
@param - destination (Tuple[int, int]): The goal position represented as a tuple of row and column indices.

@returns - Tuple[List[Tuple[int, int]], str] or None: A tuple containing the path from source to destination as a list of
        tuples representing the row and column indices. The second element of the tuple is a string representing the
        directions of the path using the characters 'L' (left), 'R' (right), 'U' (up), and 'D' (down). If there is
        no valid path, None is returned.
"""
#Imports the deque class from the collections module. 
# The deque class is a double-ended queue that provides efficient operations for adding & removing elements from both ends.
from queue import Queue 

#Takes 3 parameters: board, source, & destination: board represents the 2-D puzzle, source & destination are tuples representing the starting & goal positions.
def solve_puzzle(board, source, destination): 

    #calculates the dimensions of the puzzle board by getting len of the board (number of rows) & len of the 1st row (number of columns). 
    # It assigns the values to variables m and n respectively.
    m, n = len(board), len(board[0])

    #These data structures are used for breadth-first search traversal & keeping track of visited positions.

    #STEP 1: Create an empty queue to store the cells to be explored.
    #Using deque, we are appending elements to the right side of the queue using the append method (queue.append(new_pos)) 
    # & removing elements from the left side of the queue using the popleft method (curr_pos = queue.popleft()).
    # By appending to the right and removing from the left, we maintain the order of exploration in a first-in, first-out (FIFO) manner, 
    # which is essential for the breadth-first search (BFS) algorithm. 
    # It ensures that we explore the cells level by level, starting from the source cell and gradually moving outward.
	#The popleft operation in a deque has a time complexity of O(1), making it efficient for removing elements from the left end. This allows us to process the cells in the order they were added to the queue, following the BFS traversal strategy.

    queue = Queue()
    queue.put(source)

    #STEP 2: Create an empty set to keep track of visited cells.
    visited = set([source])

    #maps each direction ('L', 'R', 'U', 'D') to its corresponding coordinate change
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)} 

    #STEP 3: Create a dictionary to store the path from each cell to its previous cell.
    path = {} #will store the path from each position to its previous position


    # loop iterates as long as there are positions in the queue
    #While the queue is not empty:
    #We continue the traversal as long as there are cells in the queue that need to be explored. 
    # If the queue becomes empty, it means we have explored all reachable cells and haven't found the destination.


    while not queue.empty():
        #STEP 4a: Dequeue a cell from the front of the queue.
        # It dequeues the position from the left side of the queue & assigns it to curr_pos variable
        curr_pos = queue.get()

        #Check if the current position is the destination. 
        # If it is, it means we have found a valid path from the source to the destination. 
        # We can then reconstruct the path & direction string. 



        """In a BFS traversal, the algorithm explores cells in a breadth-first manner, 
        meaning it visits all cells at the current level before moving on to the next level. This ensures that the first time the destination cell is encountered during the traversal, it is reached by following the shortest path."""
        if curr_pos == destination:
            #STEP 4b: If the dequeued cell is the destination cell, return its path.
            path_list = []
            direction_str = ''

            while curr_pos != source:
                path_list.append(curr_pos)
                prev_pos = path[curr_pos]
                dx, dy = prev_pos[0] - curr_pos[0], prev_pos[1] - curr_pos[1]

                if dx == 0 and dy == -1:
                    direction_str += 'R'
                elif dx == 0 and dy == 1:
                    direction_str += 'L'
                elif dx == -1 and dy == 0:
                    direction_str += 'D'
                elif dx == 1 and dy == 0:
                    direction_str += 'U'

                curr_pos = prev_pos

            path_list.append(source)
            path_list.reverse()
            direction_str = direction_str[::-1]

            return path_list, direction_str

        for direction, (dx, dy) in directions.items():
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

            if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n and board[new_pos[0]][new_pos[1]] == '-' and new_pos not in visited:
                #STEP 4cii(a): Enqueue the neighboring cell into the queue.
                queue.put(new_pos)

                #STEP 4cii(i): Mark the cell as visited.
                visited.add(new_pos)

                #STEP 4cii(ii): Store the current cell as the previous cell for the neighboring cell.
                path[new_pos] = curr_pos

    # If the queue becomes empty and the destination cell is not reached, return None (no valid path found).
    return None


source=(0, 2)
goal=(2, 2)
Puzzle = [ ['-', '-', '-', '-', '-'], ['-', '-', '#', '-', '-'], ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-'], ['-', '#', '-', '-', '-'] ]


puzzle2 =[
    ['-', '#', '-'],
    ['-', '#', '-'],
    ['-', '#', '-']
]
# (0, 0)
# (2, 2)
puzzle3 = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

print(solve_puzzle(Puzzle, source, goal))
# print(solve_puzzle(puzzle2, (0, 0), (2, 2)))
# print(solve_puzzle(puzzle3, (0, 2), (3, 0)))

