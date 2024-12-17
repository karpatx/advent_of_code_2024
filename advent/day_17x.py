# https://topaz.github.io/paste/#XQAAAQAnCgAAAAAAAAA0m0pnuFI8c/fBNApcL1Y57OP2oKnxTxvyIghSqAWpPBtbao2Hb+AP2j9mkvrOP0Wi7vPFHukUkazZH8lxKqGQK543CkeqTUzCakD2V7NLiKOJh52PW/1LBLXNKpxtVYTHgooj94bta2sxlLBmefi5JEX0T+8Xu2zCJAbrr4cR22qPc/Y06IzgLGCn4gHZ9zNSwT9Z5tZ9o+Er+NAcDn5fUVbPKHuBwQOslqSTJ+AHJP02BZy47QnFjIP72r6mTQiO+QUGeu1i/OCVsBUN3aZptaRWtN1vKm+OZUSnFQ7Y+0+HBgpLC+iXZwIbVckHvoGLTGD0H+jKtmJzT4mv3CHIE5asFUdNVsTd+FFcwOX4N5i1zQaJIzjNI2E2IPt32bHo/DpeJ3iggBtrUUb7ANeHcdYamQVzxb2kWTwnbk5dr8kOU7sM4K2uHt7Mds0+qxm0iT5AkkFcL2X+dMFF/SvLRg4B/tsnkpPZYnoIzPnbGzgprY5I/A22oSmMPp27FS+YfNeFsk0dMvZwI5XW1hBqO3glUYRbYFtku6riwZSrPU02jzWQU4lqZd52FiS2Qwi/9012n8cNOI6+sqriJ9m/KHO7JrOTG1c9sFtwvMXanqIUND6tvuxyH+7NHOSepzXFBBB39f+tu0mdAg7zWotAuexQQdZs+/a5atiRwoluS6TmF1P6+83CZ6+162tIj3t9dgeTVH2os/+ghp4UclrpyZgFZ4rP1e2eHKB9fTubJlEgOTuno1bg7kHC50vNgb9PpTKDF/UxotZoCauAKNqCAxnh/44LPo0xwgrGb7sfmhRXKJalTSk+lCHomb6A3LoIqnU1jsbmWCoBmm/PLvYaYDHO9ImiLhz2Us70XEp77MbCjtJdUn+5NDWc6fPo6vjpN+92WkR25smYgIxNLTjFFQ9JPHxVILrUdDOuWtc7D260SiC/9d8PwaL+WFs/GqiyO4frBWy4IYqvtD1Fq4KdF3j7XHk3CIusfTFT/bn/ljTWrSHnG4EFhYH4/+NDnNY=
import sys
import re

nre = re.compile(r'(\d+)')
def GetNums(x):
    return list(map(int, nre.findall(x)))

def adv(arg):
    global IP, A
    A = A // 2**arg
    IP += 2
    return

def bxl(arg):
    global IP, B
    B ^= P[IP+1]
    IP += 2
    return

def bst(arg):
    global IP, B
    B = arg % 8
    IP += 2
    return

def jnz(arg):
    global IP, A
    if A == 0:
        IP += 2
        return
    else:
        IP = P[IP+1]
    return

def bxc(arg):
    global IP, B
    B ^= C
    IP += 2
    return

def out(arg):
    global IP, Output
    arg %= 8
    Output.append(arg)
    IP += 2
    return

def bdv(arg):
    global IP, B
    B = A // 2**arg
    IP += 2
    return

def cdv(arg):
    global IP, C
    C = A // 2**arg
    IP += 2
    return

def GetCombo(op):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return A
    elif op == 5:
        return B
    elif op == 6:
        return C
    else:
        assert False, op

I = {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}

def Solve(part2=False):
    global IP, A, B, C, Output

    NA = 0
    IP = 0
    inc = 1
    Done5 = False
    first5 = None
    Done10 = False
    first10 = None
    while True:
        if part2:
            NA += inc
            A = NA
        B = BB
        C = CC
        IP = 0
        Output = []
        while IP < len(P)-1:
            PrevOp = P[IP]
            I[P[IP]](GetCombo(P[IP+1]))
            if part2:
                if PrevOp == 5:
                    if Output != P[:len(Output)]:
                        break
                    else:
                        if Done5 == False and len(Output) == 5:
                            if first5 == None:
                                first5 = NA
                            else:
                                inc = NA - first5
                                Done5 = True
                                break
                        if Done10 == False and len(Output) == 10:
                            if first10 == None:
                                first10 = NA
                            else:
                                inc = NA - first10
                                Done10 = True
                                break
                    if Output == P:
                        return NA

        if part2 == False:
            return Output

L = sys.stdin.read().strip().split('\n')
IP = 0
A = AA = GetNums(L[0])[0]
B = BB = GetNums(L[1])[0]
C = CC = GetNums(L[2])[0]
P = GetNums(L[4])
Output = None


print(','.join(map(str, Solve(False))))
A = AA
B = BB
C = CC
IP = 0
print(Solve(True))