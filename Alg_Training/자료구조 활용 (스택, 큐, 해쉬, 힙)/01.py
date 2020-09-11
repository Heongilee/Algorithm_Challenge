import sys
from collections import deque
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N, M = map(int, input().split())

print(N)
print(M)

a = deque([])
while N != 0:
    elem = N % 10
    a.append(elem)
    N //= 10

maxV = -2147000000
for _ in range(M + 1):
    elem = a.pop()
    maxV = max(elem, maxV)
'''
############################################################
# 80점...
'''
N, M = map(int, input().split())

# int to str(원소 하나하나씩 접근 가능하게...) 하고나서 list화 시킴. 
N = deque(list(map(int, str(N))))

def top(l):
    if not l:
        return -1
    else:
        return l[len(l) - 1]
    
res = []
while N:
    elem = N.popleft()
    if(top(res) == -1):
        res.append(elem)
    else:
        while(top(res) < elem) and (top(res) != -1):
            if(M == 0):
                break
            res.pop()
            M -= 1
        res.append(elem)

for e in res:
    print(e, end='')
'''
############################################################
N, M = map(int, input().split())
N = list(map(int, str(N)))

S = []
for x in N:
    while (S) and (M > 0) and (S[-1] < x):
        S.pop()
        M -= 1
    S.append(x)

if (M != 0):
    S = S[:-M]

print(S)    # [7, 8, 2, 3]
print(''.join(map(str, S))) # 7823 (join 기능.)