import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

##############################################################################
# Solution (1% TLE in Python3, MLE in Pypy3)
#########################################################################
def check(r, c):
    return board[r - 1][c] and board[r][c - 1] and board[r - 1][c - 1]

def DFS(r, c):
    global ans
    if r == n and c == m + 1:
        print([b for b in board])
        ans += 1
        return
    
    for i in range(r, n + 1):
        for j in range((c if i == r else 1), m + 1):
            '''
            이 조건에 걸리게 되면,,,

            [1, 1]
            [1, X]      # X는 Don't care
            
            를 만나게 됐을 때인데, 여기서 하나만 1로 체크 돼서 가지를 뻗어 나가면
            2x2 넴모넴모가 만들어지게 되므로 더 뻗어 나가지 않도록 앞에서 
            continue를 걸어주는 것이다. 
            '''
            if check(i, j): continue

            board[i][j] = 1
            DFS(i, j + 1)
            board[i][j] = 0
    print([b for b in board])
    ans += 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0

    DFS(1, 1)
    print(ans)
    

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