import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    dx = [-1, 0]    #12시 9시 방향.
    dy = [0, -1]
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    D = [[0] * N for _ in range(N)]
    
    D[0][0] = board[0][0]
    for i in range(N):
        for j in range(N):
            if(i == 0 and j == 0): continue
            t = 2147000000
            for k in range(2):
                xx = i + dx[k]
                yy = j + dy[k]
                if(xx < N and yy < N and D[xx][yy] != 0 and D[xx][yy] < t):
                    t = D[xx][yy]
            D[i][j] = t + board[i][j]
    print(D[N - 1][N - 1])