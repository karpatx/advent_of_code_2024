

if __name__ == '__main__':
    from utils import read_data_file, str_to_num_list
    nums = read_data_file('../data/day_1/sample_data.txt')
    list_1 = []
    list_2 = []
    for nums_line in nums:
        ints = str_to_num_list(nums_line)
        list_1.append(ints[0])
        list_2.append(ints[1])
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    distance = 0
    for x, y in zip(list_1, list_2):
        distance += abs(x - y)
    print(distance)
    similarity = 0
    for x in list_1:
        similarity += x * list_2.count(x)
    print(similarity)