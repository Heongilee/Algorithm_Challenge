import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def minimum(M):
    t = 2147000000
    res = (-1, -1)
    for i in range(N):
        for j in range(N):
            if(M[i][j] < t):
                t = M[i][j]
                res = (i, j)
    return res 

def maximum(M):
    t = -2147000000
    res = (-1, -1)
    for i in range(N):
        for j in range(N):
            if(M[i][j] > t):
                t = M[i][j]
                res = (i, j)
    return res 

def DFS(x, y):
    global cnt
    if((x, y) == end):
        cnt += 1
    else:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if(0 <= X <= N - 1 and 0 <= Y <= N - 1 and visit[X][Y] != 1):
                visit[X][Y] = 1
                DFS(X, Y)
                visit[X][Y] = 0
        

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N = int(input())
    M = list(list(map(int, input().split())) for _ in range(N))
    visit = list([0] * N for _ in range(N))
    cnt = 0
    
    start = minimum(M)
    end = maximum(M)
    
    DFS(start[0], start[1])
    print(cnt)