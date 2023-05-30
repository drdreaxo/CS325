def minEffort(puzzle):
    m = len(puzzle)  # Number of rows
    n = len(puzzle[0])  # Number of columns

    # Initialize a 2D array to store the efforts
    efforts = [[float('inf')] * n for _ in range(m)]
    efforts[0][0] = 0  # Effort of starting cell is 0

    # Create a queue for BFS traversal
    queue = [(0, 0)]

    # Define the possible directions to move
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
