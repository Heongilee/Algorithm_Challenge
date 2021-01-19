# Floyd-Warshall_Algorithm 
# Big-O : O(n^3)
###################################################################
# D(a, b) = min(D(a, b), D(a, k) + D(k, b))
###################################################################
# 다익스트라 알고리즘과 차이점은 
# 1. 출발 노드 설정이 필요없고,
# 2. 매 라운드 마다 모든 노드로의 최단 거리를 계산할 필요가 없다.

import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
INF = int(1e9)

def floydWarshall():
    for i in range(n + 1):
        for j in range(n + 1):
            if(i == j):
                continue
            for k in range(n + 1):
                if(i == k or j == k):
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    # 자기 자신으로 가는 간선은 없다.
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    
    # 알고리즘 수행
    floydWarshall()

    # 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(graph[i][j] == INF):
                print("INF", end=" ")
            else:
                print(graph[i][j], end=" ")
        print()