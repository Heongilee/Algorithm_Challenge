import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
def odd(x):
    return True if (x % 2 !=0) else False

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

i = 0
j = N // 2
sum = 0
for k in range(N):
    size = (N // 2) if(odd(k)) else (N // 2 + 1)
    
    l = i
    m = j
    for _ in range(size):
        sum += a[l][m]
        l += 1
        m -= 1
    if(odd(k)):
        j += 1
    else:
        i += 1
print(sum)
'''
###################################################################
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
S = E = N // 2
flag = True
sum = 0
for i in range(N):
    for j in range(S, E + 1):
       sum += a[i][j]
    if(E - S + 1 >= N):
        flag = False
    if(flag):
        S -= 1
        E += 1
    else:
        S += 1
        E -= 1
print(sum)