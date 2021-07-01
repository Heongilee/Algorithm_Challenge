import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

def findParent(v):
    if v != parent[v]:
        v = findParent(parent[v])
    return parent[v]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    
    for _ in range(m):
        u, v = map(int, input().split())

        if findParent(u) != findParent(v):
            unionParent(u, v)
    
    S = set()
    for i in range(1, n + 1): S.add(findParent(i))
    print(len(S))
    