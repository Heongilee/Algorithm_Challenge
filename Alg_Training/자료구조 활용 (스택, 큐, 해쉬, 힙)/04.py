import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

a = input()
S = []
for e in a:
    if e.isdecimal():
        S.append(int(e))
    else:
        ope2 = int(S.pop())
        ope1 = int(S.pop())
        if(e == '+'):
            res = ope1 + ope2
        elif(e == '-'):
            res = ope1 - ope2
        elif(e == '*'):
            res = ope1 * ope2
        else:
            res = ope1 / ope2
        S.append(res)
else:
    print(S.pop())