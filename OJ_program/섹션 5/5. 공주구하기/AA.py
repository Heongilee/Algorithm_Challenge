from collections import deque
N, K = map(int, input().split())

Q = deque([])

def enqueue(Q, e):
    Q.append(e)

def dequeue(Q):
    res = Q.popleft()
    return res

## Main
for i in range(1, N + 1):
    enqueue(Q, i)

cnt = 0
while (len(Q) != 1):
    cnt += 1
    if(cnt == K):
        dequeue(Q)
        cnt = 0
    else:
        enqueue(Q, dequeue(Q))
print(dequeue(Q))