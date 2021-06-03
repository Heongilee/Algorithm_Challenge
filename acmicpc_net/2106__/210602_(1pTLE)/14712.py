import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(L, i, j, one):
    global cnt
    '''
    cut-edge

    (n * m) - L은 앞으로 결정해야할 칸의 개수, one은 현재 board에서 1의 개수
    즉, 앞으로 남은 칸의 개수에 전부 1을 채워넣는다고 해도 4를 넘지 못한다면
    더 가지를 뻗어나갈 필요가 없다.
    '''
    if (n * m) - L + one < 4: return
    if j >= m: i, j = i + 1, 0
    if i >= n:
        if any ((board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]) for i in range(n - 1) for j in range(m - 1)):
            cnt += 1
        return

    board[i][j] = 0
    DFS(L + 1, i, j + 1, one)
    board[i][j] = 1
    DFS(L + 1, i, j + 1, one + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())    # 1 ≤ N, M ≤ 25, 1 ≤ N × M ≤ 25
    board = [[0] * m for _ in range(n)]

    tot = 2 ** (n * m)  # 33,554,432
    cnt = 0
    DFS(0, 0, 0, 0)
    print(tot - cnt)