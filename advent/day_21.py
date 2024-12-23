from typing import List, Tuple

#SHORT_INPUTS = ['029A', '980A', '179A', '456A', '379A']
SHORT_INPUTS = ['456A']
REAL_INPUTS = ['826A', '341A', '582A', '983A', '670A']

NUMPAD_COORDS = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2),
    'invalid': (3,0)
}
DIRPAD_COORDS = {
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
    'invalid': (0,0)
}

#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#<<vA>>^A<A>AvA<^AA>A<vAAA>^A
#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

def manhattan_distance(p0: Tuple[int, int], p1: Tuple[int, int]) -> int:
    return abs(p0[0]-p1[0]) + abs(p0[1]-p1[1])

def move_from_to(design: dict, current: Tuple[int, int], target: str) ->str:
    movements = ''
    y, x = current[0], current[1]
    target_coords = design[target]
    while target_coords != (y,x):
        print(y, x, movements)
        if x < target_coords[1] and (y, x+1) != design['invalid']:
            x += 1
            movements += '>'
        elif x > target_coords[1] and (y, x-1) != design['invalid']:
            x -= 1
            movements += '<'
        elif y < target_coords[0] and (y+1, x) != design['invalid']:
            y += 1
            movements += 'v'
        elif y > target_coords[0] and (y-1, x) != design['invalid']:
            y -= 1
            movements += '^'
    #print(manhattan_distance(current, design[target]), len(movements))
    return movements, (y,x)


if __name__ == '__main__':
    all = 0
    for input in SHORT_INPUTS:
        print(input)
        start = (3,2)
        s = ''
        for c in input:
            m, start = move_from_to(NUMPAD_COORDS, start, c)
            s += m
            s += 'A'
        print('1', s, len(s))
        start = (0,2)
        s2 = ''
        for c in s:
            m, start = move_from_to(DIRPAD_COORDS, start, c)
            s2 += m
            s2 += 'A'
        print('2', s2, len(s2))
        start = (0,2)
        s3 = ''
        for c in s2:
            m, start = move_from_to(DIRPAD_COORDS, start, c)
            s3 += m
            s3 += 'A'
        print('3', s3, len(s3))
        code = int(input.replace('A', ''))
        print(code, len(s3), code * len(s3))
        all += code * len(s3)
    print(all)