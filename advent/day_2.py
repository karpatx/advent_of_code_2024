from typing import List, Tuple


def calculate_diffs(nums: List[int]) -> List[int]:
    return [nums[x+1] - nums[x] for x in range(0, len(nums) - 1)]

def step_too_large(nums: List[int]) -> Tuple[bool, List[bool]]:
    p_map = [(abs(x) > 3 or x == 0) for x in nums]
    return any(p_map), p_map

def step_direction_change(nums: List[int]) -> Tuple[bool, List[bool]]:
    if nums[0] > 0:
        p_map = [x < 0 for x in nums]
        if p_map.count(False) == 1:
            return any(p_map), [not x for x in p_map]
        return any(p_map), p_map
    p_map = [x > 0 for x in nums]
    if p_map.count(False) == 1:
        return any(p_map), [not x for x in p_map]
    return any(p_map), p_map

def bad_list(nums: List[int]) -> bool:
    nums_diffs = calculate_diffs(nums)
    too_large, _ = step_too_large(nums_diffs)
    direction_change, _ = step_direction_change(nums_diffs)
    return too_large or direction_change

def solution(nums: List[int]) -> bool:
    print(nums)
    for index in range(0, len(nums)):
        mod_nums = nums.copy()
        mod_nums.pop(index)
        print(mod_nums, index, bad_list(mod_nums))
        if not bad_list(mod_nums):
            return True
    return False
        

if __name__ == '__main__':
    from .utils import read_data_file, str_to_num_list
    nums = read_data_file('../data/day_2/sample_data.txt')
    nums_int = [str_to_num_list(x) for x in nums]
    diffs_int = [calculate_diffs(x) for x in nums_int]
    print(len(nums_int))
    right = len(nums_int)
    for index, diffs in enumerate(diffs_int):
        too_large, too_large_map = step_too_large(diffs)
        direction_change, direction_change_map = step_direction_change(diffs)
        all_map = [x or y for x,y in zip(too_large_map, direction_change_map)]
        if too_large or direction_change:
            #if all_map.count(True) == 1:
            if solution(nums_int[index]):
                pass
            else:
                right -= 1
    print(right)
