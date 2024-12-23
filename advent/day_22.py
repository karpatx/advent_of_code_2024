from typing import Tuple
from utils import read_data_file

def proc(secret: int) -> int:
    mix_this = secret << 6
    secret ^= mix_this
    secret %= 16777216
    mix_this = secret >> 5
    secret ^= mix_this
    secret %= 16777216
    mix_this = secret << 11
    secret ^= mix_this
    secret %= 16777216
    return secret


if __name__ == '__main__':
    secret_list = [1, 10, 100, 2024]

    original_file = read_data_file('../data/day_22/sample_data.txt')
    secret_list.clear()

    for line in original_file:
        secret_list.append(int(line))

    result = 0
    for i, s in enumerate(secret_list):
        print(i, end='\r')
        for _ in range(0, 2000):
            s = proc(s)
        #print(s)
        result += s
    print(result)

    buyers_changes = []
    for i, s in enumerate(secret_list):
        print(i, end='\r')
        changes_list = []
        last_s = s
        for i in range(0, 2000):
            s = proc(s)
            #if i > 0:
            changes_list.append(((s % 10), (s % 10) - (last_s % 10)))
            last_s = s
        buyers_changes.append(changes_list)
    patterns = {}
    max_result = 0
    for index in range(0, len(buyers_changes[0])-4):
        p = (buyers_changes[0][index], buyers_changes[0][index+1], buyers_changes[0][index+2], buyers_changes[0][index+3])
        if (p[0][1], p[1][1], p[2][1], p[3][1]) not in patterns:
            patterns[(p[0][1], p[1][1], p[2][1], p[3][1])] = True
            result = buyers_changes[0][index+3][0]
            for b_c in buyers_changes[1:]:
                pattern_found = None
                for i in range(0, len(b_c)-4):
                    if b_c[i][1] == p[0][1] and b_c[i+1][1] == p[1][1] and b_c[i+2][1] == p[2][1] and b_c[i+3][1] == p[3][1]:
                        result += b_c[i+3][0]
                        break
            if result > max_result:
                max_result = result
        print(max_result)
