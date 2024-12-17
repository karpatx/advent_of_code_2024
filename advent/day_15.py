from typing import List, Tuple
from copy import deepcopy

from utils import get_yx, set_yx, find_char

MAP: List[List[str]] = []
MOVEMENTS: List[str] = []
MOVEMENT_CODES = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def convert_map(m: List[List[str]]) -> List[List[str]]:
    converted = []
    for y in range(0, len(m)):
        row = []
        for x in range(0, len(m[y])):
            val = get_yx(m, y, x)
            if val == '@':
                row += ['@', '.']
            elif val == 'O':
                row += ['[]']
            else:
                row += [val] * 2
        converted.append(row)
    return converted

def part_1():
    step = 0
    for movement in ''.join(MOVEMENTS):
        robot_coords = find_char(MAP, '@')
        move_these = []
        next_y = robot_coords[0]
        next_x = robot_coords[1]
        while True:
            move_these.append({'from': (next_y, next_x), 'to': (next_y+MOVEMENT_CODES[movement][0], next_x+MOVEMENT_CODES[movement][1])})
            next_y += MOVEMENT_CODES[movement][0]
            next_x += MOVEMENT_CODES[movement][1]
            if get_yx(MAP, next_y, next_x) == 'O':
                continue
            break
        move_these.reverse()
        if get_yx(MAP, move_these[0]['to'][0], move_these[0]['to'][1]) == '.':
            for move in move_these:
                f = get_yx(MAP, move['from'][0], move['from'][1])
                t = get_yx(MAP, move['to'][0], move['to'][1])
                set_yx(MAP, move['to'][0], move['to'][1], f)
                set_yx(MAP, move['from'][0], move['from'][1], t)
        step += 1
        print(step)
        for line in MAP:
            print(''.join(line))
    all = 0
    for y in range(0, len(MAP)):
        for x in range(0, len(MAP[y])):
            if get_yx(MAP, y, x) == 'O':
                all += y*100 + x
    print(all)

def rec(matrix: List[List[str]], move: str, to_y: int, to_x: int, already: dict, move_these: List):
    print(move_these, to_y, to_x, get_yx(matrix, to_y, to_x), '/', already, '/')
    if len(move_these) == 0:
        return
    if get_yx(matrix, to_y, to_x) == '#':
        move_these.clear()
        return
    if get_yx(matrix, to_y, to_x) == '.':
        return
    from_y, from_x = to_y, to_x
    to_y += MOVEMENT_CODES[move][0]
    to_x += MOVEMENT_CODES[move][1]
    if get_yx(matrix, from_y, from_x) == '[':
        m = {'from': (from_y, from_x), 'to': (to_y, to_x)}
        key = f'{from_y}-{from_x}'
        if key not in already:
            move_these.append(m)
        rec(matrix, move, to_y, to_x, already, move_these)
        m = {'from': (from_y, from_x+1), 'to': (to_y, to_x+1)}
        key = f'{from_y}-{from_x+1}'
        if key not in already:
            move_these.append(m)
        rec(matrix, move, to_y, to_x+1, already, move_these)
    elif get_yx(matrix, from_y, from_x) == ']':
        m = {'from': (from_y, from_x), 'to': (to_y, to_x)}
        key = f'{from_y}-{from_x+1}'
        if key not in already:
            move_these.append(m)
        rec(matrix, move, to_y, to_x, already, move_these)
        m = {'from': (from_y, from_x-1), 'to': (to_y, to_x-1)}
        key = f'{from_y}-{from_x-1}'
        if key not in already:
            move_these.append(m)
        rec(matrix, move, to_y, to_x-1, already, move_these)

if __name__ == '__main__':
    from utils import read_data_file
    original_file = read_data_file('../data/day_15/sample_data_small.txt')

    for i, line in enumerate(original_file):
        if line == '':
            MOVEMENTS = original_file[i+1:]
            break
        MAP.append(list(line))
    original_map = deepcopy(MAP)

    #part_1()    
    
    converted_map = convert_map(original_map)
    for line in converted_map:
        print(''.join(line))

    step = 0
    for movement in ''.join(MOVEMENTS):
        robot_coords = find_char(converted_map, '@')
        move_these = []
        next_y = robot_coords[0]
        next_x = robot_coords[1]
        if movement == '<' or movement == '>':
            while True:
                if movement == '<' or movement == '>':
                    move_these.append({'from': (next_y, next_x), 'to': (next_y+MOVEMENT_CODES[movement][0], next_x+MOVEMENT_CODES[movement][1])})
                    next_y += MOVEMENT_CODES[movement][0]
                    next_x += MOVEMENT_CODES[movement][1]
                    if get_yx(converted_map, next_y, next_x) == '[' or get_yx(converted_map, next_y, next_x) == ']':
                        continue
                    break
            move_these.reverse()
            if get_yx(converted_map, move_these[0]['to'][0], move_these[0]['to'][1]) == '.':
                for move in move_these:
                    f = get_yx(converted_map, move['from'][0], move['from'][1])
                    t = get_yx(converted_map, move['to'][0], move['to'][1])
                    set_yx(converted_map, move['to'][0], move['to'][1], f)
                    set_yx(converted_map, move['from'][0], move['from'][1], t)
        else:
            move_these.append({'from': (next_y, next_x), 'to': (next_y+MOVEMENT_CODES[movement][0], next_x+MOVEMENT_CODES[movement][1])})
            rec(converted_map, movement, next_y+MOVEMENT_CODES[movement][0], next_x+MOVEMENT_CODES[movement][1], {f'{next_y}-{next_x}: 1'}, move_these)
            if len(move_these) != 0:
                #if movement == '^':
                #    move_these = sorted(move_these, key=lambda x: x['to'][0])
                #else:
                #    move_these = sorted(move_these, key=lambda x: x['to'][0], reverse=True)
                move_these.reverse()
                print(move_these)
                for move in move_these:
                    f = get_yx(converted_map, move['from'][0], move['from'][1])
                    t = get_yx(converted_map, move['to'][0], move['to'][1])
                    set_yx(converted_map, move['to'][0], move['to'][1], f)
                    set_yx(converted_map, move['from'][0], move['from'][1], t)
        step += 1
        if step == 23:
            break
        print(step)
        for line in converted_map:
            print(''.join(line))
    all = 0
    for y in range(0, len(converted_map)):
        for x in range(0, len(converted_map[y])):
            if get_yx(converted_map, y, x) == '[':
                all += y*100 + x
    print(all)
