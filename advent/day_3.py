

if __name__ == '__main__':
    from re import finditer
    from utils import read_data_file
    garbage = read_data_file('../data/day_3/sample_data.txt')
    summary = 0
    turned_on = True
    for match in finditer(r'(mul\([0-9]{1,}\,[0-9]{1,}\))|(do\(\))|(don\'t\(\))', str(garbage)):
        eval = match.group()
        if eval == 'do()':
            turned_on = True
        elif eval == 'don\'t()':
            turned_on = False
        elif turned_on:
            eval = eval.replace('mul(', '').replace(')', '').split(',')
            summary += int(eval[0]) * int(eval[1])
    print(summary)