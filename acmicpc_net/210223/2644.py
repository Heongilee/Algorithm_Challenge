# 백준 2644번
# https://www.acmicpc.net/problem/2644
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

def DFS(L, u):
    global res
    if u == v:
        res = L
        return
    else:
        for e in tree[u]:
            if not visited[e]:
                visited[e] = True
                DFS(L + 1, e)

if __name__ == '__main__':
    n = int(input())
    u, v = map(int, input().split())
    m = int(input())
    tree = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    res = -1
    
    for _ in range(m):
        x, y = map(int, input().split())

        tree[x].append(y)
        tree[y].append(x)
    
    visited[u] = True
    DFS(0, u)
    print(res)
