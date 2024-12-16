from typing import List, Tuple

def str_to_num_list(line: str) -> List[int]:
    return [int(x) for x in line.split(' ') if x != '']

def read_data_file(file_name: str) -> List[str]:
    with open(file_name, 'r') as f_read:
        return [x.strip() for x in f_read if x != '']

def get_yx(m: List[List[str]], y: int, x: int):
    if y<0 or x<0 or y>=len(m) or x>=len(m[0]):
        #print(y, x, len(m), len(m[0]))
        return ''
    return m[y][x]

def set_yx(m: List[List[str]], y: str, x: str, a: str):
    if y < 0 or x < 0 or y >= len(m) or x >= len(m[0]):
        return False
    m[y][x] = a
    return True

def find_char(m: List[List[str]], char_to_find: str) ->Tuple[int, int]:
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if get_yx(m, y, x) == char_to_find:
                return (y, x)
    return (-1, -1)
