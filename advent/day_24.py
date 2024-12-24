from typing import Tuple
from itertools import combinations
from utils import read_data_file

REGS = {}
PRG = []

if __name__ == '__main__':

    original_file = read_data_file('../data/day_24/sample_data.txt')

    half = False
    for line in original_file:
        if line == '':
            half = True
            continue
        if not half:
            d = line.split(':')
            REGS[d[0].strip()] = d[1].strip()
        else:
            d = line.split('->')
            target = d[1].strip()
            sources = d[0].split(' ')
            s0 = sources[0].strip()
            s1 = sources[2].strip()
            key = f'{sources[0]}-{sources[2]}'
            prg = {
                'target': target,
                's0': s0,
                's1': s1,
                'operand': sources[1].strip()
            }
            PRG.append(prg)
            if target not in REGS:
                REGS[target] = None
            if s0 not in REGS:
                REGS[s0] = None
            if s1 not in REGS:
                REGS[s1] = None

    run = True
    while run:
        for prg in PRG:
            s0 = REGS[prg['s0']]
            s1 = REGS[prg['s1']]
            if s0 is not None and s1 is not None:
                if prg['operand'] == 'OR':
                    REGS[prg['target']] = '1' if s0 == '1' or s1 == '1' else '0'
                elif prg['operand'] == 'AND':
                    REGS[prg['target']] = '1' if s0 == '1' and s1 == '1' else '0'
                elif prg['operand'] == 'XOR':
                    REGS[prg['target']] = '1' if s0 != s1 else '0'
                else:
                    raise('Invalid operand')

        run = False
        for k, v in REGS.items():
            if k.startswith('z') and v is None:
                run = True
                break

    z_s = ''
    keys = sorted(REGS.keys())
    for k in keys:
        print(k, REGS[k])
        if k.startswith('z'):
            z_s += REGS[k]
    print(z_s[::-1], int(z_s[::-1], 2))
