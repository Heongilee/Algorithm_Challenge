import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

a = input()
S = []
res = ''

for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            S.append(x)
        elif x == '*' or x == '/':
            while S and (S[-1] == '*' or S[-1] == '/'):
                res += S.pop()
            S.append(x)
        elif x == '+' or x == '-':
            while S and (S[-1] != '('):
                res += S.pop()
            S.append(x)
        elif x == ')':
            while S and (S[-1] != '('):
                res += S.pop()
            S.pop()
else:
    while S:
        res += S.pop()
print(res)