# 백준 1992번
# https://www.acmicpc.net/problem/1992
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

#영역 안의 요소가 전부 1이면 1, 0이면 0 섞여있으면 -1
def elementChecker(x1, x2, y1, y2):   
    flag = -1
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] != flag and flag != -1:
                return -1
            elif board[i][j] != flag and flag == -1:
                flag = board[i][j]
    return flag

def DFS(x1, x2, y1, y2):
    t = elementChecker(x1, x2, y1, y2)
    if t != -1:
        print(t, end='')
        return
    else:
        Xmid, Ymid = (x2 + x1) // 2, (y2 + y1) // 2
        print("(", end='')
        DFS(x1, Xmid, y1, Ymid)
        DFS(x1, Xmid, Ymid + 1, y2)
        DFS(Xmid + 1, x2, y1, Ymid)
        DFS(Xmid + 1, x2, Ymid + 1, y2)
        print(")", end='')

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    DFS(0, n - 1, 0, n - 1)
    print()