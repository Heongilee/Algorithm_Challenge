import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    N, M = map(int, input().split())    # N개의 노드, M개의 간선
    
    # 그래프의 약자 g (인덱스는 1 ~ N 까지 사용할거임. 그래서 N + 1)
    g = [[0] * (N + 1) for _ in range(N + 1)]
    
    # 무 방향 간선 그래프 초기화
    for _ in range(M):
        a, b, v = map(int, input().split())
        g[a][b] = v
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(g[i][j], end=' ')
        print()
    
