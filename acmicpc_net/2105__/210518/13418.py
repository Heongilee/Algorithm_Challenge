import sys, heapq as hq
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

def findParent(v):
    if parent[v] != v:
        parent[v] = findParent(parent[v])
    return parent[v]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def unionFind(pq):
    global parent
    hq.heapify(pq)
    parent = list(range(n + 1))
    cnt = 0
    while pq:
        c, a, b = hq.heappop(pq)
        c = -c

        if findParent(a) != findParent(b):
            unionParent(a, b)
            if c == 0: cnt += 1

    return cnt ** 2

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m + 1)]
    parent = []
    print(unionFind([(c, a, b) for a, b, c in roads if c == 0]) - unionFind([(-c, a, b) for a, b, c in roads]))