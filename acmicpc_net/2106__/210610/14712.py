import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 0, -1, -1]
dy = [0, -1, 0, -1]
def DFS(i, j):
    global cnt

    if i == n - 1 and j == m:
        print([b for b in board])
        cnt += 1
        return

    for k in range(i, n):
        for l in range((j if i == k else 0), m):
            if k > 0 and l > 0:
                if all (board[k + dx[m]][l + dy[m]] for m in range(4)): continue
            board[k][l] = 1
            DFS(k, l + 1)

            board[k][l] = 0
            DFS(k, l + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    cnt = 0

    board[0][0] = 1
    DFS(0, 1)
    board[0][0] = 0
    DFS(0, 1)

    print(2 ** (n * m), cnt)

##############################################################################
# Python MLE, Pypy3 TLE
#########################################################################
'''
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
def DFS(i, j):
    global cnt
    if j >= m: i, j = i + 1, 0
    if i >= n:
        for k in range(n - 2 + 1):
            for l in range(m - 2 + 1):
                if all (board[k + dx[m]][l + dy[m]] for m in range(4)):
                    # print([b for b in board])
                    cnt += 1
                    return
        return

    board[i][j] = 0
    DFS(i, j + 1)
    board[i][j] = 1
    DFS(i, j + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    cnt = 0

    board[0][0] = 0
    DFS(0, 1)
    board[0][0] = 1
    DFS(0, 1)

    # print(2 ** (n * m), cnt)
    print(2 ** (n * m) - cnt)
'''