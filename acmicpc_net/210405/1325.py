import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
input = sys.stdin.readline

def BFS(v):
    dq = deque()
    dq.append(v)
    visited = [False] * (n + 1)
    visited[v] = True
    cnt = 1

    while dq:
        t = dq.popleft()
        visited[t] = True

        for node in graph[t]:
            if not visited[node]:
                cnt += 1
                visited[node] = True
                dq.append(node)
    return cnt
            
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    res = []
    M = 0

    # build graph
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)
    
    # excute BFS algorithm
    for i in range(1, n + 1):
        if graph[i]:
            r = BFS(i)
            if r >= M:
                if r > M:
                    M = r
                    res = []
                res.append(i)
    print(*res)
