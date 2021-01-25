# 백준 2252번
# https://www.acmicpc.net/problem/2252
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    I = [0] * (n + 1)
    dq = deque([])

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        I[b] += 1
    
    for i in range(1, n + 1):
        if(I[i] == 0):
            dq.append(i)
    
    while(dq):
        t = dq.popleft()
        print(t, end=' ')
        for e in graph[t]:
            I[e] -= 1
            if(I[e] == 0):
                dq.append(e)
    print()