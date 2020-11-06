import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

def DFS(x, y):
    xx = x
    yy = y
    
    while(True):
        if((0 <= yy + dy[1] < 10) and board[xx][yy + dy[1]] == 1 and visit[xx][yy + dy[1]] == 0):
            while((0 <= yy + dy[1] < 10) and (board[xx][yy + dy[1]] != 0)):
                xx += dx[1]
                yy += dy[1]
                visit[xx][yy] = 1
            DFS(xx, yy)
        elif((0 <= yy + dy[3] < 10) and board[xx][yy + dy[3]] == 1 and visit[xx][yy + dy[3]] == 0):
            while((0 <= yy + dy[3] < 10) and (board[xx][yy + dy[3]] != 0)):
                xx += dx[3]
                yy += dy[3]
                visit[xx][yy] = 1
            DFS(xx, yy)
        else:
            if(xx == 0):
                print(yy)
                sys.exit(0)
            # move forward
            xx += dx[0]
            yy += dy[0]
            visit[xx][yy] = 1

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    board = [list(map(int, input().split())) for _ in range(10)]
    visit = [[0] * 10 for _ in range(10)]
    
    for i in range(10):
        for j in range(10):
            if(board[i][j] == 2):
                visit[i][j] = 1
                DFS(i, j)