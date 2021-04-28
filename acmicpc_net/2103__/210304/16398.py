# 백준 16398번
# https://www.acmicpc.net/problem/16398
import sys
import heapq as hq
sys.stdin = open("./acmicpc_net/input.txt", "rt")


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
    pq = []
    parent = list(range(n + 1))
    res = 0

    for i in range(n):
        t = list(map(int, input().split()))
        for j in range(n):
            if(t[j] == 0):
                continue
            hq.heappush(pq, (t[j], i + 1, j + 1))

    while pq:
        w, a, b = hq.heappop(pq)

        if findParent(a) != findParent(b):
            unionParent(a, b)
            res += w

    print(res)
