from copy import deepcopy
from typing import List, Tuple

def unpack(original: str) -> List[int]:
    print(len(original[0]))
    unpacked = []
    original_list = list(''.join(original))
    oid = 0
    for i in range(0, len(original_list)):
        if i%2 == 0:
            if original_list[i] != '0':
                unpacked += [oid for _ in range(int(original_list[i]))]
            oid += 1
        else:
            if original_list[i] != '0':
                unpacked += [-1 for _ in range(int(original_list[i]))]
    return unpacked

def find_next_free(disk: List[int], p: int) ->int:
    while disk[p] != -1:
        p += 1
    return p

def find_next_free_len(disk: List[int], p: int) ->Tuple[int, int]:
    while p < len(disk) - 1 and disk[p] != -1:
        p += 1
    start = p
    while start < len(disk) - 1 and disk[start] == -1:
        start += 1
    return p, start - p

def find_last_occupied(disk: List[int], p: int) ->int:
    while p > 0 and disk[p] == -1:
        p -= 1
    return p

def find_last_occupied_start_len(disk: List[int], p: int) ->Tuple[int, int]:
    if disk[p] == -1:
        while p > 0 and disk[p] == -1:
            p -= 1
    start = p
    while disk[start] == disk[p]:
        start -= 1
    return start + 1, p - start

def rearrange(disk: List[int]):
    target_pointer = find_next_free(disk, 0)
    source_pointer = find_last_occupied(disk, len(disk) - 1)
    while source_pointer >= target_pointer:
        disk[target_pointer], disk[source_pointer] = disk[source_pointer], disk[target_pointer]
        target_pointer = find_next_free(disk, target_pointer)
        source_pointer = find_last_occupied(disk, source_pointer)
    print(len(disk), target_pointer, source_pointer)

def rearrange2(disk: List[int]):
    files_list = []
    p = len(disk) - 1
    while p > 0:
        s, l = find_last_occupied_start_len(disk, p)
        files_list.append({'start': s, 'length': l, 'value': disk[s]})
        p = s - 1
    while len(files_list) > 0:
        print(files_list[0])
        next, next_len = find_next_free_len(disk, 0)
        while True:
            if next_len >= files_list[0]['length'] and next < files_list[0]['start']:
                i = 0
                while i < files_list[0]['length']:
                    disk[next + i] = files_list[0]['value']
                    disk[files_list[0]['start'] + i] = -1
                    i += 1
                #print(disk)
                break
            next, next_len = find_next_free_len(disk, next + next_len)
            if next >= len(disk) or next_len == 0:
                break
        files_list = files_list[1:]


def checksum(disk: List[int]) -> int:
    result = 0
    p = 0
    while p < len(disk):
        if disk[p] != -1:
            result += p * disk[p]
        p += 1
    return result

if __name__ == '__main__':
    from utils import read_data_file
    original_file = read_data_file('../data/day_9/sample_data.txt')
    raw_disk = unpack(original_file)
    unpacked = deepcopy(raw_disk)
    #print(raw_disk)
    rearrange(raw_disk)
    #print(raw_disk)
    result = checksum(raw_disk)
    print(result)
    #print(unpacked)
    rearrange2(unpacked)
    #print(unpacked)
    result = checksum(unpacked)
    print(result)
