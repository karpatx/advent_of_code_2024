from typing import List
from utils import read_data_file, get_yx

KEYS = []
LOCKS = []

def parse_lock(m: List[List[str]]) ->List[str]:
    lock = []
    for x in range(0, len(m[0])):
        for y in range(1,len(m)):
            if get_yx(m, y, x) == '.':
                lock.append(str(y-1))
                break
    return lock

def parse_key(m: List[List[str]]) ->List[str]:
    key = []
    for x in range(0, len(m[0])):
        for y in range(1,len(m)):
            if get_yx(m, y, x) == '#':
                key.append(str(len(m) - y - 1))
                break
    return key

if __name__ == '__main__':

    original_file = read_data_file('../data/day_25/sample_data.txt')

    lock, key = False, False
    current = []
    for line in original_file:
        if line == '':
            if lock:
                LOCKS.append(parse_lock(current))
            elif key:
                KEYS.append(parse_key(current))
            current = []
            lock, key = False, False
        elif not lock and not key:
            if line.startswith('#'):
                lock = True
                current = [list(line)]
            else:
                key = True
                current = [list(line)]
        else:
            current.append(list(line))

    ok = 0
    for lock in LOCKS:
        for key in KEYS:
            fit = True
            print(lock, key, end='')
            for i in range(0, len(key)):
                #print(i, key[i], lock[i], int(key[i]) + int(lock[i]) > 5)
                if int(key[i]) + int(lock[i]) > 5:
                    #print('hellomi')
                    fit = False
            print(fit)
            if fit:
                ok += 1
    
    print('OK:', ok)
