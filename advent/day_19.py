from typing import List, Dict
from functools import lru_cache

from utils import read_data_file

PATTERNS: Dict[str, bool]
DESIGNS: List[str]
SOLUTIONS: Dict[str, int] = {}
MEM = {}

@lru_cache(maxsize=50)
def rec(current: int, original_design: str, longest: int):
    for index, i in enumerate(range(longest, 0, -1)):
        if len(design[current:current+i]) > 0:
            if design[current:current+i] in PATTERNS:
                rec(current + i, original_design, longest)
        else:
            break
    if current == len(original_design):
        if original_design in SOLUTIONS:
            SOLUTIONS[original_design] += 1
        else:
            SOLUTIONS[original_design] = 1

def rec2(design, cache={}):
    print(design, cache)
    if design in cache:
        return cache[design]

    if len(design) == 0:
        cache[design] = 1
        return 1
    count = 0
    for i, o in enumerate(PATTERNS):
        if design.startswith(o):
            r = rec2(design[len(o):], cache)
            count += r
            print('*', i, o, r)
    cache[design] = count
    return count

if __name__ == '__main__':
    lines = read_data_file('../data/day_19/sample_data_small.txt')
    PATTERNS = {x.strip(): True for x in lines[0].split(',')}
    DESIGNS = [x.strip() for x in lines[2:]]

    maximum = max([len(x) for x in PATTERNS.keys()])

    part_1 = False
    if part_1:
        counter = 0
        all = 0
        for design in DESIGNS:
            rec(0, design, maximum)
            print(design, SOLUTIONS[design] if design in SOLUTIONS else 0)
            if design in SOLUTIONS:
                counter += 1
                all += SOLUTIONS[design]
        print(counter)
        print(all)
    else:
        result = 0 
        for d in DESIGNS:
            result += rec2(d)
        print(result)
