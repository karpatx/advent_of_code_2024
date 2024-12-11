from copy import deepcopy
from typing import List, Tuple

VELOCITIES = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

def create_matrix(lines: List[str]) -> List[List[str]]:
    matrix: List[List[str]] = []
    for line in lines:
        matrix.append(list(line))
    return matrix

def get_xy(matrix: List[List[str]], y: int, x: int) -> str:
    if x < 0 or y < 0 or y > len(matrix) - 1 or x > len(matrix[y]) - 1:
        return ''
    return matrix[y][x]

def set_xy(matrix: List[List[str]], y: int, x: int, value: str) -> bool:
    if x < 0 or y < 0 or y > len(matrix) - 1 or x > len(matrix[y]) - 1:
        return False
    matrix[y][x] = value
    return True

def simulate(base_matrix: List[List[str]], sy: int, sx: int) -> Tuple[List[List[str]], int]:
    matrix = deepcopy(base_matrix)
    steps = 0
    velocity = 0
    while get_xy(matrix, sy, sx) != '':
        set_xy(matrix, sy, sx, 'X')
        sx += VELOCITIES[velocity][1]
        sy += VELOCITIES[velocity][0]
        if get_xy(matrix, sy, sx) == '#':
            sx -= VELOCITIES[velocity][1]
            sy -= VELOCITIES[velocity][0]
            velocity += 1
            velocity %= 4
        steps += 1
        if steps > len(matrix) * len(matrix[0]) * 30:
            return matrix, steps
    return matrix, steps

if __name__ == '__main__':
    from utils import read_data_file
    floor_base = read_data_file('../data/day_6/sample_data.txt')
    floor_matrix = create_matrix(floor_base)
    coord_x = -1
    coord_y = -1
    for y in range(0, len(floor_matrix)):
        for x in range(0, len(floor_matrix[y])):
            if get_xy(floor_matrix, y, x) == '^':
                coord_x = x
                coord_y = y
    matrix, steps = simulate(floor_matrix, coord_y, coord_x)
    x_es = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if get_xy(matrix, y, x) == 'X':
                x_es += 1
    print(x_es, steps)
    counter = 0
    for y in range(0, len(floor_matrix)):
        for x in range(0, len(floor_matrix[y])):
            if get_xy(floor_matrix, y, x) == '.':
                copied_floor_matrix = deepcopy(floor_matrix)
                set_xy(copied_floor_matrix, y, x, '#')
                _, steps = simulate(copied_floor_matrix, coord_y, coord_x)
                if steps > len(matrix) * len(matrix[0]) * 30:
                    print(y, x, steps)
                    counter += 1
    print(counter)
    #for fl in floor_matrix:
    #    print(''.join(fl))
