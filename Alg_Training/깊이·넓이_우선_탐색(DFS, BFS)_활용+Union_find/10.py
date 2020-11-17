import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Success
Case #05 : Success

점수 결과 : 100
'''
'''
def DFS(x, y):
    global cnt
    if((x, y) == end):
        cnt += 1
    else:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if(0 <= X <= N - 1 and 0 <= Y <= N - 1 and visit[X][Y] != 1 and M[X][Y] != 1):
                visit[X][Y] = 1
                DFS(X, Y)
                visit[X][Y] = 0

if __name__ == '__main__':
    N = 7
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    M = list(list(map(int, input().split())) for _ in range(N))
    visit = list([0] * N for _ in range(N))
    cnt = 0
    
    start = (0, 0)
    end = (N - 1, N - 1)
    visit[start[0]][start[1]] = 1
    DFS(start[0], start[1])
    print(cnt)
'''
##########################################################################
def DFS(x, y):
    global cnt
    if(x == 6 and y == 6):
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if(0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] != 1):
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0
                
if __name__ == '__main__':
    board = list(list(map(int, input().split())) for _ in range(7))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)