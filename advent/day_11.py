from typing import List

SMALL_DATA = '125 17'
ORIGINAL_DATA = '92 0 286041 8034 34394 795 8 2051489'

cache = {}

def rec(value: str, num: int):
    key = f'{value}-{num}'
    if key in cache:
        return cache[key]
    if num == 0:
        cache[key] = 1
        return 1
    if value == '0':
        result = rec('1', num - 1)
        return result
    elif len(value) % 2 == 0:
        result = rec(str(int(value[:len(value) // 2])), num - 1) +  rec(str(int(value[len(value) // 2:])), num - 1)
        cache[key] = result
        return result
    result = rec(str(int(value) * 2024), num - 1)
    cache[key] = result
    return result




if __name__ == '__main__':
    source_str = ORIGINAL_DATA
    steps = 75
    original_source = source_str.split(' ')
    all = 0
    for value in original_source:
        all += rec(value, steps)
    print(all)
