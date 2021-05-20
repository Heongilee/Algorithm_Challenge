import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 행이나 열중에서 가장 긴 캔디를 리턴함.
def longestCandy(board):
    global ans
    # 가로
    for i in range(n):
        candy = board[i][0]
        length = 1
        for j in range(1, n):
            if candy == board[i][j]:
                length += 1
            else:
                if length > ans: ans = length
                length = 1
                candy = board[i][j]
        if length > ans: ans = length
    
    # 세로
    for j in range(n):
        myList = [board[i][j] for i in range(n)]
        candy = myList[0]
        length = 1
        for i in range(1, n):
            if candy == myList[i]:
                length += 1
            else:
                if length > ans: ans = length
                length = 1
                candy = myList[i]
        if length > ans: ans = length

def DFS(L, board):
    global ans
    if L == 1:
        longestCandy(board)
        return

    for i in range(n):
        for j in range(n - 1):
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            DFS(L + 1, board)
            board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]
    
    for i in range(n - 1):
        for j in range(n):
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            DFS(L + 1, board)
            board[i + 1][j], board[i][j] = board[i][j], board[i + 1][j]

if __name__ == '__main__':
    n = int(input())
    ans = 0
    DFS(0, [list(input().rstrip()) for _ in range(n)])
    print(ans)