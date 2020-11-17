import sys
import time
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")


def minimum_position():
    t = 2147000000
    x = -1
    y = -1
    for i in range(n):
        for j in range(n):
            if(m[i][j] < t):
                t = m[i][j]
                x = i
                y = j
    return x, y

def maximum_position():
    t = -2147000000
    x = -1
    y = -1
    for i in range(n):
        for j in range(n):
            if(m[i][j] > t):
                t = m[i][j]
                x = i
                y = j
    return x, y

def DFS(x, y):
    global cnt
    if((x, y) == end):
        cnt += 1
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if(0 <= xx < n and 0 <= yy < n and m[xx][yy] > m[x][y] and chk[xx][yy] != 1):
                chk[xx][yy] = 1
                DFS(xx, yy)
                chk[xx][yy] = 0

if __name__ == "__main__":
    start_time = time.time()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    chk = [[0] * n for _ in range(n)]
    cnt = 0
    
    start = minimum_position()  #Tuple
    end = maximum_position()    #Tuple
    
    chk[start[0]][start[1]] = 1
    DFS(start[0], start[1])
    print(cnt)
    end_time = time.time()
    print(f"time : {round(end_time - start_time, 10)}sec")
