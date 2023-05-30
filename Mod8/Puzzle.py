from collections import deque

def solve_puzzle(board, source, destination):
    m, n = len(board), len(board[0])
    queue = deque([source])
    visited = set([source])
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    path = {}

    while queue:
        curr_pos = queue.popleft()

        if curr_pos == destination:
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
                queue.append(new_pos)
                visited.add(new_pos)
                path[new_pos] = curr_pos

    return None


source=(0, 2)
goal=(2, 2)
Puzzle = [ ['-', '-', '-', '-', '-'], ['-', '-', '#', '-', '-'], ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-'], ['-', '#', '-', '-', '-'] ]

print(solve_puzzle(Puzzle, source, goal))

