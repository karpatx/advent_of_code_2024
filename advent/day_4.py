from typing import List

COORDS = [
    ((1, 0), (2, 0), (3, 0)),
    ((-1, 0), (-2, 0), (-3, 0)),
    ((0, 1), (0, 2), (0, 3)),
    ((0, -1), (0, -2), (0, -3)),
    ((1, 1), (2, 2), (3, 3)),
    ((-1, -1), (-2, -2), (-3, -3)),
    ((-1, 1), (-2, 2), (-3, 3)),
    ((1, -1), (2, -2), (3, -3)),
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

def mas(matrix: List[List[str]], y: int, x: int) -> bool:
    if get_xy(matrix, y, x) != 'A':
        return False
    nw = get_xy(matrix, y - 1, x - 1)
    ne = get_xy(matrix, y - 1, x + 1)
    sw = get_xy(matrix, y + 1, x - 1)
    se = get_xy(matrix, y + 1, x + 1)
    if ((nw == 'S' and se == 'M') or (nw == 'M' and se == 'S')) and ((sw == 'S' and ne == 'M') or (sw == 'M' and ne == 'S')):
        return True
    return False

if __name__ == '__main__':
    from utils import read_data_file
    xmas_base = read_data_file('../data/day_4/sample_data.txt')
    xmas_matrix = create_matrix(xmas_base)
    xmas_counter = 0
    mas_counter = 0
    for y in range(0, len(xmas_matrix)):
        for x in range(0, len(xmas_matrix[y])):
            if mas(xmas_matrix, y, x):
                mas_counter += 1
            if get_xy(xmas_matrix, y, x) != 'X':
                continue
            for coords in COORDS:
                if get_xy(xmas_matrix, y + coords[0][0], x + coords[0][1]) != 'M':
                    continue
                if get_xy(xmas_matrix, y + coords[1][0], x + coords[1][1]) != 'A':
                    continue
                if get_xy(xmas_matrix, y + coords[2][0], x + coords[2][1]) == 'S':
                    xmas_counter += 1
    print(xmas_counter)
    print(mas_counter)
