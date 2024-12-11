from itertools import product


lines = []
with open('sample_data.txt', 'r') as f_read:
    for line in f_read:
        l0 = line.strip().split(':')
        lines.append([l0[0]] + [x for x in l0[1].strip().split(' ')])

result = 0
for line in lines:
    for operators in product(['+', '*'], repeat=len(line)-2):
        all = int(line[1])
        for x, y in zip(line[2:], list(operators)):
            if y == '+':
                all += int(x)
            else:
                all *= int(x)
        if all == int(line[0]):
            result += all
            break
print(result)

result = 0
for line in lines:
    for operators in product(['+', '*', '||'], repeat=len(line)-2):
        all = int(line[1])
        for x, y in zip(line[2:], list(operators)):
            if y == '+':
                all += int(x)
            elif y == '||':
                all = int(str(all) + x)
            else:
                all *= int(x)
        if all == int(line[0]):
            result += all
            break
print(result)
