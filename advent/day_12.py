from typing import List
from copy import deepcopy

from utils import get_yx, set_yx

FACING = [1, 3, 4, 2]
AREAS = {}
ALL = {}

def fill(m: List[List[str]], y: int, x: int, value: str, area: dict):
    if value == '':
        return
    if (y, x) in ALL:
        return
    if get_yx(m, y, x) == value:
        ALL[(y, x)] = value
        area[(y,x)] = value
    else:
        return
    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        fill(m, y + move[0], x + move[1], value, area)

def calc_fence(area: dict) -> int:
    fence = 0
    for k in area.keys():
        for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (k[0] + move[0], k[1] + move[1]) not in area:
                fence += 1
    return fence

def calc_fence2(area: dict) -> int:
    fence = 0
    facing = {1:[], 2:[], 3:[], 4:[]}
    for k in area.keys():
        for move, face in zip([(-1, 0), (1, 0), (0, -1), (0, 1)], FACING):
            if (k[0] + move[0], k[1] + move[1]) not in area:
                facing[face].append((k[0] + move[0], k[1] + move[1]))
    faces = facing[1]
    if len(faces) > 0:
        fence += 1
        f = sorted(faces, key = lambda x: (x[0], x[1]))
        index = 0
        while index < len(f) - 1:
            if f[index][0] == f[index + 1][0] and abs(f[index][1] - f[index + 1][1]) == 1:
                pass
            else:
                fence += 1
            index += 1
    faces = facing[3]
    if len(faces) > 0:
        fence += 1
        f = sorted(faces, key = lambda x: (x[0], x[1]))
        index = 0
        while index < len(f) - 1:
            if f[index][0] == f[index + 1][0] and abs(f[index][1] - f[index + 1][1]) == 1:
                pass
            else:
                fence += 1
            index += 1
    
    faces = facing[2]
    if len(faces) > 0:
        fence += 1
        f = sorted(faces, key = lambda x: (x[1], x[0]))
        index = 0
        while index < len(f) - 1:
            if f[index][1] == f[index + 1][1] and abs(f[index][0] - f[index + 1][0]) == 1:
                pass
            else:
                fence += 1
            index += 1
    faces = facing[4]
    if len(faces) > 0:
        fence += 1
        f = sorted(faces, key = lambda x: (x[1], x[0]))
        index = 0
        while index < len(f) - 1:
            if f[index][1] == f[index + 1][1] and abs(f[index][0] - f[index + 1][0]) == 1:
                pass
            else:
                fence += 1
            index += 1
    return fence


if __name__ == '__main__':
    from utils import read_data_file
    original_file = read_data_file('../data/day_12/sample_data.txt')
    matrix = []
    for line in original_file:
        matrix.append(list(line))
    all = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            AREAS[(y,x)] = {}
            fill(matrix, y, x, get_yx(matrix, y, x), AREAS[(y,x)])
            if len(AREAS[(y,x)]) == 0:
                del AREAS[(y,x)]
    all = 0
    for k in AREAS.keys():
        all += len(AREAS[k]) * calc_fence(AREAS[k])
        print(k, len(AREAS[k]), len(AREAS[k]) * calc_fence(AREAS[k]))
    print(all)

    all = 0
    for k in AREAS.keys():
        fence2 = calc_fence2(AREAS[k])
        all += len(AREAS[k]) * fence2
        print(k, len(AREAS[k]), len(AREAS[k]) * fence2)
    print(all)
