# 백준 1992번
# https://www.acmicpc.net/problem/1922
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
import heapq as hq

def findParent(e):
    if(e != parent[e]):
        parent[e] = findParent(parent[e])
    return parent[e]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    parent = list(range(n + 1))
    pq = []
    cost = 0

    for _ in range(m):
        a, b, c = map(int, input().split())

        hq.heappush(pq, (c, a, b))
    
    while pq:
        c, a, b = hq.heappop(pq)

        if(findParent(a) != findParent(b)):
            unionParent(a, b)
            cost += c
    
    print(cost)
    