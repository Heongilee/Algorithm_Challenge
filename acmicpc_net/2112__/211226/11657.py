import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
def bellman_ford(start):
    dist[start] = 0
    
    for i in range(n):  # 원래는 n - 1번 순회하면 되지만, 음의 사이클을 찾기 위해 n번 순회함
        # 매 반복마다 모든 간선을 확인함.
        for j in range(m):
            cur, next_node, cost = edges[j]
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은지 확인.
            if dist[cur] != INF and dist[cur] + cost < dist[next_node]:
                dist[next_node] = dist[cur] + cost
                # * n번째 라운드에서도 값이 갱신된다면 음의 순환이 존재한다는 뜻이다.
                if i == n - 1:
                    return True
    return False
            

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    dist = [INF] * (n + 1)
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        
        edges.append((a, b, c))
    
    negative_cycle = bellman_ford(1)    # 1번 노드가 시작점
    
    if negative_cycle:
        print(-1)
    else:
        print("\n".join(map(str, [-1 if dist[i] == INF else dist[i] for i in range(2, n + 1)])))