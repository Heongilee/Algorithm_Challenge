import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
INF = int(1e9)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())

        graph[a][b] = 1
    a = 1
    k, x = map(int, input().split())

    # 자기 자신으로 가는건 0
    for i in range(1, n + 1):
        graph[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(i == j):
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    print(graph[a][x])