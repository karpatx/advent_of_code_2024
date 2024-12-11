from typing import List
from copy import deepcopy

from utils import get_yx, set_yx

def rec(m: List[List[str]], y: int, x: int, counter: List[int]):
    if get_yx(m, y, x) == '9':
        #if (y, x) not in counter:
        counter.append((y, x))
        print('hellomi')
        return
    val = int(get_yx(m, y, x))
    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        char = get_yx(m, y + move[0], x + move[1])
        if char != '':
            #print(i, ':', y + move[0], x + move[1], int(char), val + 1, int(char) == val + 1)
            if int(char) == val + 1:
                #print(y, x, int(char))
                rec(m, y + move[0], x + move[1], counter)


if __name__ == '__main__':
    from utils import read_data_file
    original_file = read_data_file('../data/day_10/sample_data.txt')
    matrix = []
    for line in original_file:
        matrix.append(list(line))
    all = 0
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            count = []
            if get_yx(matrix, y, x) == '0':
                rec(matrix, y, x, count)
                print(y, x, count)
                all += len(count)
    print(all)
