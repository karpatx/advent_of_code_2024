from typing import List, Tuple
from copy import deepcopy

from utils import get_yx, set_yx, find_char


# Python program for A* Search Algorithm
import heapq

# Define the Cell class

MAP: List[List[str]] = []

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
    return get_yx(MAP, y, x) == '.' or get_yx(MAP, y, x) == 'E' or get_yx(MAP, y, x) == 'S' or get_yx(MAP, y, x) == '1' or get_yx(MAP, y, x) == '2'

# Check if a cell is the destination
def is_destination(y, x, dest):
    return y == dest[0] and x == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(y, x, dest):
    return ((y - dest[0]) ** 2 + (x - dest[1]) ** 2) ** 0.5

# Trace the path from source to destination


def trace_path(cell_details, dest):
    #print("The Path is ")
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
        #if get_yx(MAP, path[i][0], path[i][1]) == '1' and get_yx(MAP, path[i+1][0], path[i+1][1]) != '2':
        #    return 0, ''
        ddy = path[i+1][0] - path[i][0]
        ddx = path[i+1][1] - path[i][1]
        #if dy != ddy:
        #    score += 1000 * abs(ddy-dy)
        #elif dx != ddx:
        #    score += 1000 * abs(ddx-dx)
        #else:
        score += 1
        dx = ddx
        dy = ddy
        #print(i, path[i], score)
    drawing = ''
    for y in range(0, len(MAP)):
        for x in range(0, len(MAP[y])):
            printed = False
            for i in path:
                if i[0] == y and i[1] == x:
                    drawing += 'O'
                    printed = True
                    break
            if not printed:
                drawing += get_yx(MAP, y, x)
        drawing += '\n'
    #if '1' in drawing:
    #    print(drawing.index('1'))
    #    return 0, ''
    #if '2' in drawing:
    #    print(drawing.index('2'))
    #    return 0, ''
    return score, drawing
            

# Implement the A* search algorithm
def a_star_search(src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return 0, ''

    # Check if the source and destination are unblocked
    if not is_unblocked(src[0], src[1]) or not is_unblocked(dest[0], dest[1]):
        print("Source or the destination is blocked")
        return 0, ''

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return 0,''

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
    #step = 0
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        #set_yx(MAP, WALLS[step][0], WALLS[step][1], '#')
        #step += 1
        #print(step)
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
            #print(new_y, new_x, is_valid(new_y, new_x), is_unblocked(new_y, new_x), not closed_list[new_y][new_x], dest, is_destination(new_y, new_x, dest))

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_y, new_x) and is_unblocked(new_y, new_x) and not closed_list[new_y][new_x]:
                # If the successor is the destination
                if is_destination(new_y, new_x, dest):
                    # Set the parent of the destination cell
                    cell_details[new_y][new_x].parent_y = y
                    cell_details[new_y][new_x].parent_x = x
                    #print("The destination cell is found")
                    # Trace and print the path from source to destination
                    score, drawing = trace_path(cell_details, dest)
                    return score, drawing
                else:
                    # Calculate the new f, g, and h values
                    #m_y = abs(new_y - cell_details[y][x].parent_y)
                    #m_x = abs(new_x - cell_details[y][x].parent_x)
                    #print(m_y, m_x)
                    g_new = cell_details[y][x].g + 1.0 # * (10.0 if m_x == 1 and m_y == 1 else 1.0)
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
    return 0, ''


if __name__ == '__main__':
    from utils import read_data_file
    original_file = read_data_file('../data/day_20/sample_data_small.txt')

    for line in original_file:
        MAP.append(list(line.strip()))

    original_map = deepcopy(MAP)


    stored_scores = []
    start = find_char(MAP, 'S')
    end = find_char(MAP, 'E')
    #rec(original_map, start, facing, 0, stored_scores)
    #print(stored_scores)
    already_tried = {}
    #set_yx(MAP, 7, 6, '1')
    #set_yx(MAP, 7, 5, '2')
    for x in MAP:
        print(''.join(x))
    base_score, d = a_star_search(start, end)

    #print(base_score, d)
    #asdadads
    print('base', base_score)
    scores = {}
    for y in range(0, len(MAP)):
        for x in range(0, len(MAP[y])):
            for coords in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                MAP = deepcopy(original_map)
                tried = (y, x, y + coords[0], x + coords[1])
                tried2 = (y + coords[0], x + coords[1], y, x)
                if (tried not in already_tried and tried2 not in already_tried) and get_yx(MAP, y, x) in ('#', 'E') and get_yx(MAP, y + coords[0], x + coords[1]) in ('#', 'E'):
                    set_yx(MAP, y, x, '1')
                    set_yx(MAP, y + coords[0], x + coords[1], '2')
                    score, drawing = a_star_search(start, end)
                    #print(score)
                    gain = base_score - score
                    already_tried[tried] = score
                    already_tried[tried2] = score
                    if gain != 0 and gain != base_score:
                        print('gain', gain, '\n', drawing)
                        scores[gain] = scores.get(gain, 0) + 1
    #print(already_tried)
    keys = sorted(scores.keys(), reverse=True)
    for k in keys:
        print(f'gain: {k}, times: {scores[k]}')
