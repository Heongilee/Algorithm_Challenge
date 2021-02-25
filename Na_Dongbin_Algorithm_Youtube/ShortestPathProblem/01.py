import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
import heapq as hq
INF = int(1e9)

def dijkstra(start):
    # 출발 정점에 대한 처리
    hq.heappush(pq, (0, start))
    distance[start] = 0
    
    while(pq):
        dist, now = hq.heappop(pq)
        # 현재 노드가 가지는 최단 거리가 이미 진짜 최단 거리라면 값을 구하지 않는다.
        if(distance[now] < dist):
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if(cost < distance[j[0]]):
                distance[j[0]] = cost
                # 갱신된 비용을 노드와 함께 다시 우선순위큐에 삽입한다. (아직 이게 최단 거리가 아닐수도 있기 때문.)
                hq.heappush(pq, (cost, j[0]))

if __name__ == '__main__':
    n, m, start = map(int, input().split())
    graph = [[] * (n + 1) for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    pq = []
    
    # build graph
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    # execute algorithm
    dijkstra(start)

    city = n - 1 - distance[1:].count(INF)
    time = max(distance[1:])
    # print solution
    print(city, time)
