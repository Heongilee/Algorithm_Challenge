import sys, itertools as it, copy as cp
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

'''
3 ≤ N, M ≤ 50
1 ≤ K ≤ 6
1 ≤ A[i][j] ≤ 100
1 ≤ s
1 ≤ r-s < r < r+s ≤ N
1 ≤ c-s < c < c+s ≤ M
'''
def rotateBoard(r, c, s):
    x, y = r - s - 1, c - s - 1
    tmp = board[x][y]
    # 9시
    while x < r + s - 1:
        board[x][y] = board[x + 1][y]
        x += 1
    # 6시
    while y < c + s - 1:
        board[x][y] = board[x][y + 1]
        y += 1
    # 3시
    while x > r - s - 1:
        board[x][y] = board[x - 1][y]
        x -= 1
    # 12시
    while y > c - s:
        board[x][y] = board[x][y - 1]
        y -= 1
    board[x][y] = tmp

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = None

    board_copy = cp.deepcopy(board)
    command = [list(map(int, input().split())) for _ in range(k)]
    for X in it.permutations(command, k):
        # 배열 조작
        for r, c, s in X:
            while s > 0:
                rotateBoard(r, c, s)
                s -= 1
        t = min(map(lambda i: sum(board[i]), range(n)))
        res = min(res, t) if res != None else t
        board = cp.deepcopy(board_copy)
    print(res)