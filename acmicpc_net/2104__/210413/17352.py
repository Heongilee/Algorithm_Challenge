import sys, itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def findParent(v):
    if v != parent[v]:
        parent[v] = findParent(parent[v])
    return parent[v]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    n = int(input())
    parent = list(range(n + 1))
    S = set()

    for _ in range(n - 2):
        a, b = map(int, input().split())

        if findParent(a) != findParent(b):
            unionParent(a, b)
    
    for x, y in it.combinations(range(1, n + 1), 2):
        if findParent(x) != findParent(y):
            print(x, y)
            break
