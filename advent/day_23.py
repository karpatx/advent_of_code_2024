from typing import Tuple
from itertools import combinations
from utils import read_data_file

PAIRS = {}


if __name__ == '__main__':

    original_file = read_data_file('../data/day_23/sample_data.txt')

    for line in original_file:
        d = line.split('-')
        if d[0] in PAIRS:
            if d[1] not in PAIRS[d[0]]:
                PAIRS[d[0]].append(d[1])
        else:
            PAIRS[d[0]] = [d[1]]
        if d[1] in PAIRS:
            if d[0] not in PAIRS[d[1]]:
                PAIRS[d[1]].append(d[0])
        else:
            PAIRS[d[1]] = [d[0]]
    
    THREES = {}
    for k in PAIRS.keys():
        for pair in combinations(PAIRS[k], 2):
            if k in PAIRS[pair[0]] and PAIRS[pair[1]] and pair[1] in PAIRS[pair[0]]:
                key_a = sorted([k, pair[0], pair[1]])
                key = f'{key_a[0]}-{key_a[1]}-{key_a[2]}'
                if key_a[0].startswith('t') or key_a[1].startswith('t') or key_a[2].startswith('t'):
                    THREES[key] = THREES.get(key, 0) + 1

    print(len(THREES.keys()))

    ALLS = {}
    for main_index, k in enumerate(PAIRS.keys()):
        print(main_index, k)
        for comb in range(2, len(PAIRS[k])):
            for index, sets in enumerate(combinations(PAIRS[k], comb)):
                check_set = [k] + list(sets)
                all_in = True
                for i in range(0, len(check_set)):
                    for j in range(i + 1, len(check_set)):
                        #print(check_set[i], check_set[j], check_set[j] in PAIRS[check_set[i]])
                        if check_set[j] not in PAIRS[check_set[i]]:
                            all_in = False
                            break
                #print(index, check_set, all_in)
                if all_in:
                    key_a = sorted(check_set)
                    key = ','.join(key_a)
                    #if key_a[0].startswith('t') or key_a[1].startswith('t') or key_a[2].startswith('t'):
                    ALLS[key] = ALLS.get(key, 0) + 1

    print(sorted(ALLS.keys(), key=lambda x: len(x), reverse=True)[0])
