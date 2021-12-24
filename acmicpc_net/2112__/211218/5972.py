# BOJ 5972 :: 택배배송(https://www.acmicpc.net/problem/5972)
import sys, heapq as hq
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

'''
N개의 헛간
M개의 소들의 길이 양 방향으로 그려져 있고 각 길은 C[i] 마리의 소가 있습니다. 
'''
def dijkstra(start_node):
    queue = []
    
    hq.heappush(queue, (0, start_node))
    distance[start_node] = 0
    
    while queue:
        dist, now = hq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for node, fee in graph[now]:
            cost = dist + fee
            if cost < distance[node]:
                distance[node] = cost
                hq.heappush(queue, (cost, node))
            
INF = int(10e9)
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dijkstra(1)
    print(distance[n])