import sys
from collections import deque
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

#############################################################
# BFS의 문제 특징
# * 최단 거리를 구할 때.
#############################################################
'''
def BFS(S):
    global Q
    Lv = 0
    while(len(Q) != 0):
        res = Q.popleft()
        if(res == E):
            return Lv
        chk[res] = 1
        if(0 <= res - 1 <= N and chk[res - 1] != 1):
            dis[res - 1] = dis[res] + 1
            Q.append(res - 1)
        if(0 <= res + 1 <= N and chk[res + 1] != 1):
            dis[res + 1] = dis[res] + 1
            Q.append(res + 1)
        if(0 <= res + 5 <= N and chk[res + 5] != 1):
            dis[res + 5] = dis[res] + 1
            Q.append(res + 5)
        Lv += 1
    return None

if __name__ == '__main__':
    S, E = map(int, input().split())
    N = max(S, E)
    Q = deque([])
    dis = [0] * (N + 1)
    chk = [0] * (N + 1)
    
    Q.append(S)
    dis[S] = 0
    res = BFS(S)
    print(res) 
'''
########################################################################
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
s, e = map(int, input().split())
ch[s] = 1
dis[s] = 0
dQ = deque()
dQ.append(s)

# BFS 
while(dQ):
    now = dQ.popleft()
    
    if(now == e):
        break
    for next in (now - 1, now + 1, now + 5):
        if (0 < next <= MAX) and (ch[next] == 0):
            dQ.append(next)
            ch[next] = 1
            dis[next] = dis[now] + 1
print(dis[e])