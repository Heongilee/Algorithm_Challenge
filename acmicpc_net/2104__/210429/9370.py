import sys, heapq as hq
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(s):
    D = [INF] * (n + 1) # distance
    pq = []
    hq.heappush(pq, (0, s))
    D[s] = 0
    while pq:
        dist, now = hq.heappop(pq)
        # 이미 처리된 노드라면 무시
        if D[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧으면
            if cost < D[i[0]]:
                D[i[0]] = cost
                hq.heappush(pq, (cost, i[0]))
    return D

if __name__ == '__main__':
    T = int(input())                        # 테스트 케이스 1 <= T <= 100
    
    for _ in range(T):
        n, m, t = map(int, input().split())     # 2 <= 교차로(n) <= 2,000, 1 <= 도로(m) <= 50,000, 1 <= 목적지(t) <= 100
        s, g, h = map(int, input().split())     # 1 <= 출발지(s), g와 h사이의 교차로를 지나감(g != h) <= n
        graph = [[] for _ in range(n + 1)]
        res = []

        for _ in range(m):
            a, b, d = map(int, input().split()) # 1 <= 노드(a) < 노드(b) <= n, 1 <= 도로 길이(d) <= 1000

            graph[a].append((b, d))
            graph[b].append((a, d))
        
        _s = dijkstra(s)
        _g = dijkstra(g)
        _h = dijkstra(h)
        for _ in range(t):
            x = int(input())
            # 출발지에서 g로 가는 비용(_s[g]) + g에서 h로 가는 비용(_g[h]) + h에서 도착지로 가는 비용(_h[x]) == 출발지에서 x로 가는 비용(_s[x])과 같거나,
            # 출 -> g -> h -> 도
            # 출발지에서 h로 가는 비용(_s[h]) + h에서 g로 가는 비용(_h[g]) + g에서 도착지로 가는 비용(_g[x]) == 출발지에서 x로 가는 비용(_s[x])과 같으면
            # 출 -> h -> g -> 도
            if _s[g] + _g[h] + _h[x] == _s[x] or _s[h] + _h[g] + _g[x] == _s[x]:
                res.append(x)
        # 오름차순 출력
        res.sort()
        print(' '.join(map(str, res)))