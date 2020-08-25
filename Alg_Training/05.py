import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N, K = map(int, input().split())
a = [0] * N

i = 0
cnt = 0
while True:
    if(a[i] == 0):
        cnt += 1
    if(cnt == K):
        a[i] = 1
        cnt = 0
    if(sum(a) == N - 1):
        break
    i += 1
    i %= N

for i in range(len(a)):
    if(a[i] == 0):
        print(i + 1)
        break
'''
###################################################################################
from collections import deque
N, K = map(int, input().split())

Q = deque(list(range(1, N + 1)))

def enqueue(Q, e):
    Q.append(e)

def dequeue(Q):
    res = Q.popleft()
    return res

## Main
cnt = 0
while (len(Q) != 1):
    cnt += 1
    if(cnt == K):
        dequeue(Q)
        cnt = 0
    else:
        enqueue(Q, dequeue(Q))
print(dequeue(Q))