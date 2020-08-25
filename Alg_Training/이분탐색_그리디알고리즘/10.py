import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N = int(input())
t = list(map(int, input().split()))
a = []
for i in range(len(t)):
    a.append((i + 1, t[i]))
print(a)
a.sort(key = lambda x: (x[1], x[0]))

res = []
for n, m in a:
    if(m == 0):
        res.append(n)
        continue
    current_idx = 0
    cnt = 0 # n보다 큰 값을 만난 횟수
    while (cnt < m) and (current_idx < len(res)):
        if(res[current_idx] > n):
            cnt += 1
        current_idx += 1
    res.insert(current_idx, n)
print(res)
'''
#################################################################################
'''
N = int(input())
a = list(map(int, input().split()))
seq = [0] * len(a)
for n, cnt in enumerate(a):
    n += 1
    pt = 0
    i = 0
    while(i < cnt):
        if(seq[pt] == 0):
            i += 1
        pt += 1
    while(seq[pt] != 0):
        pt += 1
    seq[pt] = n

# 출력
for e in seq:
    print(e, end=' ')
'''
####################################################################################
N = int(input())
a = list(map(int, input().split()))
seq = [0] * N

for i in range(N):
    for j in range(N):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif(seq[j] == 0):
            a[i] -= 1

for x in seq:
    print(x, end=' ')