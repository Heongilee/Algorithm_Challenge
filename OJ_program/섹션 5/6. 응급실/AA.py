from collections import deque

N, M = map(int, input().split())
tmp = list(map(int, input().split()))

Q = deque([])

def enQ(Q, e):
    Q.append(e)

def deQ(Q):
    res = Q.popleft()
    return res

def tupleMax(Q):
    mVal = -2147000000
    mIdx = -1
    for i in range(len(Q)):
        if(Q[i][1] > mVal):
            mVal = Q[i][1]
            mIdx = Q[i][0]
    return (mIdx, mVal)
            


# Main
for i in range(len(tmp)):
    enQ(Q, (i, tmp[i]))

cnt = 0
while True:
    if (M, tmp[M]) not in Q:
        break
    if (tupleMax(Q)[1] == Q[0][1]):
        deQ(Q)
        cnt += 1
    else:
        enQ(Q, deQ(Q))
print(cnt)
#######################