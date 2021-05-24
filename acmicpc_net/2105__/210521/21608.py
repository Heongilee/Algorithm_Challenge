import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
from collections import defaultdict

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(10e9)
if __name__ == '__main__':
    n = int(input())
    board = [[0] * n for _ in range(n)]
    dic = defaultdict(list)
    for line in sys.stdin:
        stu, *fav = map(int, line.rstrip().split())
        dic[stu] = fav

        maxI, maxJ = 0, 0
        maxLike, maxEmpty = -1, -1
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    like, empty = 0, 0
                    for k in range(4):
                        ii = i + dx[k]
                        jj = j + dy[k]
                        if 0 <= ii < n and 0 <= jj < n:
                            if board[ii][jj] in fav:
                                like += 1
                            if board[ii][jj] == 0:
                                empty += 1
                    if like > maxLike or (like == maxLike and empty > maxEmpty):
                        maxLike = like
                        maxEmpty = empty
                        maxI, maxJ = i, j 
        board[maxI][maxJ] = stu

    res = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                ii = i + dx[k]
                jj = j + dy[k]
                if 0 <= ii < n and 0 <= jj < n:
                    if board[ii][jj] in dic[board[i][j]]:
                        cnt += 1
            if cnt >= 1: res += 10 ** (cnt - 1)
    print(res)

##########################################################################################################
'''
아니 문제 이해가 안돼... 봐바라
↓ board
9    3    _
8    4    7
_    _    _

↓ weightBoard
0    0    1
0    0    0
1    2    2

로 만들어지면 같은 행인 2행 중에 가장 적은 열인 1이어서 (2, 1) 위치에 1이
생성되는게 맞거든? 근데 테케는 (2, 2)에 생성되네 ... 뭐야 이거 슈벌
'''
'''
if __name__ == '__main__':
    n = int(input())
    board = [[0] * n for _ in range(n)]
    dic = dict()
    for line in sys.stdin:
        weightBoard = [[0] * n for _ in range(n)]
        stu, *fav = list(map(int, line.rstrip().split()))
        dic[stu] = fav

        maxVal, x, y = 0, None, None
        for f in fav:
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 0: continue
                    if board[i][j] == f:
                        for k in range(4):
                            ii = i + dx[k]
                            jj = j + dy[k]
                            if 0 <= ii < n and 0 <= jj < n and board[ii][jj] == 0:
                                weightBoard[ii][jj] += 1
                                if weightBoard[ii][jj] > maxVal:
                                    maxVal = weightBoard[ii][jj]
                                    x, y = ii, jj
        if sum(weightBoard, []).count(maxVal) < 2:
            board[x][y] = stu
            continue

        for i in range(n):
            for j in range(n):
                if board[i][j] != 0: continue
                cnt = 0
                for k in range(4):
                    ii = i + dx[k]
                    jj = j + dy[k]
                    if 0 <= ii < n and 0 <= jj < n and board[ii][jj] == 0:
                        cnt += 1
                weightBoard[i][j] += cnt
                if weightBoard[i][j] > maxVal:
                    maxVal = weightBoard[i][j]
                    x, y = i, j
        
        if sum(weightBoard, []).count(maxVal) < 2:
            board[x][y] = stu
            continue
        
        esc = False
        for i in range(n):
            for j in range(n):
                if weightBoard[i][j] == maxVal:
                    esc = True
                    board[i][j] = stu
                    break
            if esc: break
    
    print(board)
    print(dic)
'''