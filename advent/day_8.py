from copy import deepcopy
from utils import get_yx, set_yx


M = []
ANTENNAS = {}


def print_m(m):
    for l in m:
        print(''.join(l))

with open('sample_data8.txt', 'r') as f_read:
    for line in f_read:
        M.append(list(line.strip()))

for y in range(len(M)):
    for x in range(len(M[y])):
        a = get_yx(M, y,x)
        if a != '.':
            if a in ANTENNAS:
                ANTENNAS[a].append((y,x))
            else:
                ANTENNAS[a] = [(y,x)]

M2 = deepcopy(M)
for freq, coords in ANTENNAS.items():
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            diffy = coords[i][0] - coords[j][0]
            diffx = coords[i][1] - coords[j][1]
            set_yx(M2, coords[i][0] + diffy, coords[i][1] + diffx, '#')
            set_yx(M2, coords[j][0] - diffy, coords[j][1] - diffx, '#')

result = 0
for y in range(len(M2)):
    for x in range(len(M2[y])):
        if get_yx(M2, y, x) == '#':
            result += 1
print(result)

M2 = deepcopy(M)
for freq, coords in ANTENNAS.items():
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            diffy = coords[i][0] - coords[j][0]
            diffx = coords[i][1] - coords[j][1]
            d = 0
            while set_yx(M2, coords[i][0] + diffy * d, coords[i][1] + diffx * d, '#'):
                d += 1
            d = 0
            while set_yx(M2, coords[j][0] - diffy * d, coords[j][1] - diffx * d, '#'):
                d += 1

result = 0
for y in range(len(M2)):
    for x in range(len(M2[y])):
        if get_yx(M2, y, x) == '#':
            result += 1
print(result)
