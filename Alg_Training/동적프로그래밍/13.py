import sys
sys.stdin = open("./Alg_Training/input.txt")

if __name__ == "__main__":
    N, M = map(int, input().split())
    dis = list([2147000000] * N for _ in range(N))
    for i in range(N):
        dis[i][i] = 0
    
    for i in range(M):
        v1, v2, w = map(int, input().split())
        dis[v1 - 1][v2 - 1] = w
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    
    # 출력
    for i in range(N):
        for j in range(N):
            if(dis[i][j] == 2147000000):
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
