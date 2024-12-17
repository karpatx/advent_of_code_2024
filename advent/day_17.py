from typing import List, Tuple

SMALL_PRG = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
'''

LARGE_PRG = '''Register A: 64751475
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0
'''

PART2_SMALL_PRG = '''Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0'''

def run(program: List[int], A: int, B: int, C: int) -> List[int]:
    #print(A, B, C, prg)
    output: List[int] = []
    ip = 0
    while ip < len(program):
        instruction = program[ip]
        operand = program[ip + 1]
        if operand == 4:
            operand = A
        elif operand == 5:
            operand = B
        elif operand == 6:
            operand = C
        ip_plus = 2
        if instruction == 0: # adv
            A = A // (2 ** operand)
        elif instruction == 1: # bxl
            B ^= operand
        elif instruction == 2: # bst
            B = operand % 8
        elif instruction == 3: # jnz
            if A == 0:
                pass
            else:
                ip = operand
                ip_plus = 0
        elif instruction == 4: # bxc
            B ^= C
        elif instruction == 5: # out
            output.append(operand % 8)
        elif instruction == 6: # bdv
            B = A // (2 ** operand)
        elif instruction == 7: # cdv
            C = A // (2 ** operand)
        
        ip += ip_plus
    return output


def read_prg(source: str) -> Tuple[int, int, int, List[int]]:
    A, B, C = 0, 0, 0
    prg = []
    for line in source.split('\n'):
        if line.startswith('Register'):
            d = line.replace('Register ', '').split(':')
            if d[0] == 'A':
                A = int(d[1].replace(' ', ''))
            elif d[0] == 'B':
                B = int(d[1].replace(' ', ''))
            elif d[0] == 'C':
                C = int(d[1].replace(' ', ''))
        elif line.startswith('Program'):
            prg = [int(x) for x in line.replace('Program: ', '').split(',')]
    return A, B, C, prg

if __name__ == '__main__':
    a, b, c, prg = read_prg(LARGE_PRG)
    output = run(prg, a, b, c)
    print(','.join([str(x) for x in output]))
    # part_2 https://kyle.so/writing/aoc-2024
    a = 0
    for pos in range(len(prg) - 1, -1, -1):
        a <<= 3
        while not run(prg, a, b, c) == prg[pos:]:
            print(run(prg, a, b, c), prg[pos:])
            a += 1
        print(pos, a)
    print(run(prg, a, b, c), prg)
