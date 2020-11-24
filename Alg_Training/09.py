import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(x, y):
    if(D[x][y] > 0):
        return D[x][y]
    if(x == 0 and y == 0):
        return board[0][0]
    else:
        if(y == 0):
            D[x][y] = DFS(x - 1, y) + board[x][y]
        elif(x == 0):
            D[x][y] = DFS(x, y - 1) + board[x][y]
        else:
            D[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + board[x][y]
        return D[x][y]


if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    D = [[0] * N for _ in range(N)]

    res = DFS(N - 1, N - 1)
    print(res)
