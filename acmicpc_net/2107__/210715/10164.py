import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [[i + j for j in range(m)] for i in range(1, n * m + 1, m)]
    D = [[None] * m for _ in range(n)]
    for i in range(m): D[0][i] = 1
    for i in range(n): D[i][0] = 1

    j = 1
    while j < m:
        i = 1
        while i < n:
            if D[i][j] == None:
                D[i][j] = D[i - 1][j] + D[i][j - 1]
                if board[i][j] == k:
                    for k in range(j, m): D[i][k] = D[i][j]
                    for k in range(i, n): D[k][j] = D[i][j]
                    i, j = i + 1, j + 1
                    continue
            i += 1
        j += 1
    print(D[n - 1][m - 1])