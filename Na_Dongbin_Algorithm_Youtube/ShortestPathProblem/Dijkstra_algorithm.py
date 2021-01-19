# https://youtu.be/acqm9mM1P6o
# Dijkstra algorithm
#########################################################################################
# 다익스트라 알고리즘은 그리디 알고리즘으로 분류됨.
# 또한, Dynamic Programming으로도 해결함.
# 매 상황에서 가장 비용이 적은 노드를 선택해 반복함.
#########################################################################################
# V가 노드의 개수일 때, Time Complexity는 O(V^2)이다.
# 라운드를 반복할 때 마다 선형 탐색을 하므로 10,000개의 노드일 경우 1억번의 연산이 소요됨.
#########################################################################################
# 힙 라이브러리를 사용해서 우선순위 큐를 구현한다.

import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
import heapq as hq
INF = int(1e9)

# # 방문하지 않은 노드 중에서 최단 거리인 노드 번호를 반환.
# def getSmallestNode():
#     min_value = INF
#     idx = 0
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]: # distance 배열의 최솟값을 선택하는데, visited 값이 False인 인덱스를 찾음.
#             min_value = distance[i]
#             idx = i
#     return idx

def dijkstra(start):
    pq = []
    hq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dis, node = hq.heappop(pq)
        if(distance[node] < dis):
            continue
        for i in graph[node]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(pq, (cost, i[0]))


if __name__ == '__main__':
    n, m = map(int, input().split())    # node(n), edge(m)
    start = int(input())

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    # 간선 정보 입력받기
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    # 알고리즘 수행
    dijkstra(start)

    # 출력
    print("출발 노드 =", start)
    for i in range(1, n + 1):
        print(i, "번 노드로 가기위한 최단 거리 : ", end='')
        if(distance[i] == INF): # 도달할 수 없는 경우...
            print("INF")
        else:
            print(distance[i])
    print()