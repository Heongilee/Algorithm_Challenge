# 백준 11779번
# https://www.acmicpc.net/problem/11779
import heapq as hq
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
INF = int(10e9)

def pathExpression(L, v):
    if(v == src):
        print(L)
        print(v, end=' ')
    else:
        pathExpression(L + 1, prev[v])
        print(v, end=' ')

def dijkstra():
    pq = [] # (비용, 인접노드)
    distance[src] = 0
    hq.heappush(pq, (0, src))

    while pq:
        dis, node = hq.heappop(pq)

        if(distance[node] < dis):   # 이미 최소값 갱신됐으면 넘김
            continue
        for i in graph[node]:
            cost = dis + i[1]
            if(cost <= distance[i[0]]):
                distance[i[0]] = cost
                hq.heappush(pq, (cost, i[0]))
                prev[i[0]] = node

if __name__ == '__main__':
    n = int(input())
    distance = [INF] * (n + 1)
    prev = [0] * (n + 1)    # 최소값 갱신했을때 이전노드를 기록하는 리스트
    graph = [[] for _ in range(n + 1)]
    m = int(input())
    res = []

    # build graph
    for _ in range(m):
        a, b, w = map(int, input().split()) 
        graph[a].append((b, w))

    src, des = map(int, input().split())    # 출발지, 도착지
    res.append(src)

    # execute algorithm
    dijkstra()

    # output
    print(distance[des])
    pathExpression(1, des)
    print()