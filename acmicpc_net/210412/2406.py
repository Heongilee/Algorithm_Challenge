import sys, heapq as hq
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def printWeight():
    for w in weight:
        print(w)

def findParent(x):
    if x != parent[x]:
        parent[x] = findParent(parent[x])
    return parent[x]

def unionParent(x, y):
    x = findParent(x)
    y = findParent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    n, m = map(int, input().split())    # 컴퓨터 개수, 지사 컴퓨터들의 연결 쌍의 개수
    parent = list(range(n + 1))
    X, K = 0, 0
    res = []
    
    for _ in range(m):
        x, y = map(int, input().split())

        if findParent(x) != findParent(y):
            unionParent(x, y)
            K += 1

    weight = []
    for i in range(1, n + 1):
        t = list(map(int, input().split()))
        if i == 1: continue
        for j in range(1, n + 1):
            if i >= j:
                continue
            else:
                hq.heappush(weight, (t[j - 1], i, j))

    while weight and K < n - 2:
        w, a, b = hq.heappop(weight)

        if findParent(a) != findParent(b):
            unionParent(a, b)
            res.append((a, b))
            X += w
            K += 1

    # output
    print(X, len(res))
    for r in res:
        print(r[0], r[1])