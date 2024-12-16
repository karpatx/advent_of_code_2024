from typing import List, Tuple
from copy import deepcopy

from utils import get_yx, set_yx, find_char


# Python program for A* Search Algorithm
import math
import heapq

# Define the Cell class

MOVEMENTS = {
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
    'N': (-1, 0)
}
MAP: List[List[str]] = []
DONE = {}

# used a modified version of this solution for a* https://www.geeksforgeeks.org/a-search-algorithm-in-python/

class Cell:
    def __init__(self):
    # Parent cell's row index
        self.parent_y = 0
    # Parent cell's column index
        self.parent_x = 0
    # Total cost of the cell (g + h)
        self.f = float('inf')
    # Cost from start to this cell
        self.g = float('inf')
    # Heuristic cost from this cell to destination
        self.h = 0


def is_valid(y, x):
    return (y >= 0) and (y < len(MAP)) and (x >= 0) and (x < len(MAP[y]))

# Check if a cell is unblocked


def is_unblocked(y, x):
    return get_yx(MAP, y, x) == '.' or get_yx(MAP, y, x) == 'S' or get_yx(MAP, y, x) == 'E'

# Check if a cell is the destination


def is_destination(y, x):
    return get_yx(MAP, y, x) == 'E'

# Calculate the heuristic value of a cell (Euclidean distance to destination)


def calculate_h_value(y, x, dest):
    return ((y - dest[0]) ** 2 + (x - dest[1]) ** 2) ** 0.5

# Trace the path from source to destination


def trace_path(cell_details, dest):
    print("The Path is ")
    path = []
    y = dest[0]
    x = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[y][x].parent_y == y and cell_details[y][x].parent_x == x):
        path.append((y, x))
        temp_y = cell_details[y][x].parent_y
        temp_x = cell_details[y][x].parent_x
        y = temp_y
        x = temp_x

    # Add the source cell to the path
    path.append((y, x))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    dy = 0
    dx = 1
    score = 0
    for i in range(0, len(path) - 1):
        ddy = path[i+1][0] - path[i][0]
        ddx = path[i+1][1] - path[i][1]
        if dy != ddy:
            score += 1000 * abs(ddy-dy)
        elif dx != ddx:
            score += 1000 * abs(ddx-dx)
        #else:
        score += 1
        dx = ddx
        dy = ddy
        print(i, path[i], score)
    for y in range(0, len(MAP)):
        for x in range(0, len(MAP[y])):
            printed = False
            for i in path:
                if i[0] == y and i[1] == x:
                    print('O', end='')
                    printed = True
                    break
            if not printed:
                print(get_yx(MAP, y, x), end='')
        print()
            

# Implement the A* search algorithm


def a_star_search(src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(src[0], src[1]) or not is_unblocked(dest[0], dest[1]):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1]):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = [[False for _ in range(len(MAP))] for _ in range(len(MAP[0]))]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(len(MAP))] for _ in range(len(MAP[0]))]

    # Initialize the start cell details
    y = src[0]
    x = src[1]
    cell_details[y][x].f = 0
    cell_details[y][x].g = 0
    cell_details[y][x].h = 0
    cell_details[y][x].parent_y = y
    cell_details[y][x].parent_x = x

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, y, x))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        y = p[1]
        x = p[2]
        closed_list[y][x] = True

        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                      #(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_y = y + dir[0]
            new_x = x + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_y, new_x) and is_unblocked(new_y, new_x) and not closed_list[new_y][new_x]:
                # If the successor is the destination
                if is_destination(new_y, new_x):
                    # Set the parent of the destination cell
                    cell_details[new_y][new_x].parent_y = y
                    cell_details[new_y][new_x].parent_x = x
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    m_y = abs(new_y - cell_details[y][x].parent_y)
                    m_x = abs(new_x - cell_details[y][x].parent_x)
                    #print(m_y, m_x)
                    g_new = cell_details[y][x].g + 1.0 * (10.0 if m_x == 1 and m_y == 1 else 1.0)
                    h_new = calculate_h_value(new_y, new_x, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_y][new_x].f == float('inf') or cell_details[new_y][new_x].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_y, new_x))
                        # Update the cell details
                        cell_details[new_y][new_x].f = f_new
                        cell_details[new_y][new_x].g = g_new
                        cell_details[new_y][new_x].h = h_new
                        cell_details[new_y][new_x].parent_y = y
                        cell_details[new_y][new_x].parent_x = x

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

def rec(m: List[List[str]], coords: Tuple[int, int], facing: str, score, scores: List[int]):
    #for y in range(0, len(m)):
    #    for x in range(0, len(m[y])):
    #        if y == coords[0] and x == coords[1]:
    #            print('S', end='')
    #        else:
    #            print(get_yx(m, y, x), end='')
    #    print()
    if facing == 'E' or facing == 'W':
        score += 1000
        for f in ['N', 'S']:
            next_coords = (coords[0] + MOVEMENTS[f][0], coords[1] + MOVEMENTS[f][1])
            if get_yx(m, next_coords[0], next_coords[1]) == '.':
                key = f'{f}-{coords[0]}-{coords[1]}'
                if key not in DONE:
                    DONE[key] = True
                    rec(m, next_coords, f, score, scores)
    elif facing == 'N' or facing == 'S':
        score += 1000
        for f in ['E', 'W']:
            next_coords = (coords[0] + MOVEMENTS[f][0], coords[1] + MOVEMENTS[f][1])
            if get_yx(m, next_coords[0], next_coords[1]) == '.':
                key = f'{f}-{coords[0]}-{coords[1]}'
                if key not in DONE:
                    DONE[key] = True
                    rec(m, next_coords, f, score, scores)
    coords = (coords[0] + MOVEMENTS[facing][0], coords[1] + MOVEMENTS[facing][1])
    score += 1
    val = get_yx(m, coords[0], coords[1])
    if val == 'E':
        scores.append(score)
        return
    elif val == '#' or val == '':
        return
    rec(m, coords, facing, score, scores)

if __name__ == '__main__':
    from utils import read_data_file
    original_file = read_data_file('../data/day_16/sample_data.txt')

    for line in original_file:
        MAP.append(list(line))
    original_map = deepcopy(MAP)
    for l in original_map:
        print(''.join(l))

    stored_scores = []
    facing = 'E'
    start = find_char(original_map, 'S')
    #rec(original_map, start, facing, 0, stored_scores)
    #print(stored_scores)
    end = find_char(original_map, 'E')
    a_star_search(start, end)
