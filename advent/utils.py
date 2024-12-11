from typing import List

def str_to_num_list(line: str) -> List[int]:
    return [int(x) for x in line.split(' ') if x != '']

def read_data_file(file_name: str) -> List[str]:
    with open(file_name, 'r') as f_read:
        return [x.strip() for x in f_read if x != '']

def get_yx(m, y, x):
    if y<0 or x<0 or y>=len(m) or x>=len(m[0]):
        return ''
    return m[y][x]

def set_yx(m, y, x, a):
    if y<0 or x<0 or y>=len(m) or x>=len(m[0]):
        return False
    m[y][x] = a
    return True
