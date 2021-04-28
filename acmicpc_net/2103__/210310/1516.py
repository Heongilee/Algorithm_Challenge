# 백준 1516번
# https://www.acmicpc.net/problem/1516
import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    T = [0] # 각 인덱스번째의 건물을 짓는데 걸리는 시간.
    D = [0] * (n + 1)   # 다이나믹 프로그래밍
    inDeg = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    preInfo = [[-1]]
    dq = deque()

    for i in range(1, n + 1):
        time, *l = list(map(int, input().split()))
        l = l[:len(l) - 1]
        preInfo.append(l)
        T.append(time)

        if len(l) != 0:
            for e in l:
                inDeg[i] += 1
                graph[e].append(i)

    # 진입차수가 0인 노드 계산
    for i in range(1, n + 1):
        if inDeg[i] == 0:
            dq.append(i)
    
    while dq:
        t = dq.popleft()
        D[t] = T[t] + max(map(lambda x: D[x], preInfo[t])) if preInfo[t] else T[t]

        for e in graph[t]:
            inDeg[e] -= 1
            if inDeg[e] == 0:
                dq.append(e)        
    
    for i in range(1, n + 1):
        print(D[i])