from typing import List

ADDING = 10000000000000

def win_prize2(machine: dict) -> int:
    global ADDING
    # part 2 based on this solution: https://github.com/michaelerne/adventofcode-2024/blob/main/day_13.py
    a = (machine['Buttons']['B']['X'] * machine['Prize']['Y'] - machine['Buttons']['B']['Y'] * machine['Prize']['X']) // (machine['Buttons']['A']['Y'] * machine['Buttons']['B']['X'] - machine['Buttons']['A']['X'] * machine['Buttons']['B']['Y'])
    b = (machine['Prize']['X'] - a * machine['Buttons']['A']['X']) // machine['Buttons']['B']['X']
    if (machine['Prize']['X'] - a * machine['Buttons']['A']['X']) % machine['Buttons']['B']['X'] == 0 and (machine['Buttons']['B']['X'] * machine['Prize']['Y'] - machine['Buttons']['B']['Y'] * machine['Prize']['X']) % (machine['Buttons']['A']['Y'] * machine['Buttons']['B']['X'] - machine['Buttons']['A']['X'] * machine['Buttons']['B']['Y']) == 0:
        return 3 * a + b
    return 0

def win_prize(machine: dict) -> int:
    tokens = []

    for n in range(0, 100):
        for m in range(0, 100):
            x = n * machine['Buttons']['A']['X']
            y = n * machine['Buttons']['A']['Y']
            x += m * machine['Buttons']['B']['X']
            y += m * machine['Buttons']['B']['Y']
            if x == machine['Prize']['X'] and y == machine['Prize']['Y']:
                tokens.append(3 * n + m)
    return min(tokens) if len(tokens) >= 1 else 0


if __name__ == '__main__':
    from utils import read_data_file

    list_of_machines = []
    original_file = read_data_file('../data/day_13/sample_data.txt')
    machine = {}
    for index, line in enumerate(original_file):
        if index % 4 == 0:
            d0 = line.split(',')
            d1 = d0[0].split('+')
            d2 = d0[1].split('+')
            machine['Buttons'] = {'A': {'X': int(d1[1]), 'Y': int(d2[1])}}
        elif index % 4 == 1:
            d0 = line.split(',')
            d1 = d0[0].split('+')
            d2 = d0[1].split('+')
            machine['Buttons']['B'] = {'X': int(d1[1]), 'Y': int(d2[1])}
        elif index % 4 == 2:
            d0 = line.split(',')
            d1 = d0[0].split('=')
            d2 = d0[1].split('=')
            machine['Prize'] = {'X': int(d1[1]) + ADDING, 'Y': int(d2[1]) + ADDING}
            list_of_machines.append(machine)
        else:
            machine = {}
    #print(list_of_machines)
    #list_of_machines = list_of_machines[:1]
    #print(list_of_machines)
    all_tokens = 0
    for m in list_of_machines:
        all_tokens += win_prize2(m)
    print(all_tokens)
