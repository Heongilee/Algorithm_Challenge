import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def isCoverable(k, l, x):   # k, l위치에서 x*x만큼의 색종이를 커버할 수 있는지?
    for kk in range(k, k + x):
        for ll in range(l, l + x):
            if 0 <= kk < N and 0 <= ll < N:
                if board[kk][ll] == 0:
                    return False
            else:
                return False
    return True

def DFS(L):
    global N, res, remainder, board

    if res != None and res <= L:
        return
    if remainder == 0:
        res = min(res, L) if res != None else L
        return
    
    # Step 1. 색좋이 놓을 위치를 먼저 찾고
    for i in range(N):
        for j in range(N):
            if board[i][j]: break
        if board[i][j]: break
    
    # Step 2. 색종이를 크기별로 대본다.
    if board[i][j]:
        for x in range(1, 6):
            if paper[x]:
                dq = deque()

                if isCoverable(i, j, x):
                    for ii in range(i, i + x):
                        for jj in range(j, j + x):
                            board[ii][jj] = 0
                            dq.append((ii, jj))
                    remainder -= x ** 2
                    paper[x] -= 1
                    DFS(L + 1)
                    paper[x] += 1
                    remainder += x ** 2
                    while dq:
                        ii, jj = dq.popleft()
                        board[ii][jj] = 1


if __name__ == '__main__':
    N = 10
    board = [list(map(int, input().split())) for _ in range(N)]
    res = None
    paper = [-1, 5, 5, 5, 5, 5]
    remainder = sum([board[i][j] for i in range(10) for j in range(10)])
    DFS(0)
    print(res if res != None else -1)