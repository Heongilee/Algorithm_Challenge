import sys
import copy as cp
input = sys.stdin.readline
INF = int(10e4)

def printBoard(board):
    print("---------------------------------------------")
    for b in board:
        print(b)


def solution(rows, columns, queries):
    board = [list(range(i, i + columns)) for i in range(1, rows * columns, columns)]
    res = []
    
    for x1, y1, x2, y2 in queries:
        minimum = INF
        # 인덱스 조정
        x1, x2 = x1 - 1, x2 - 1
        y1, y2 = y1 - 1, y2 - 1

        tmp = board[x1][y1]
        minimum = min(minimum, tmp)
        px, py = x1, y1
        # 아래
        while px < x2:
            board[px][py] = board[px + 1][py]
            minimum = min(minimum, board[px + 1][py])
            px += 1
        # 오른쪽
        while py < y2:
            board[px][py] = board[px][py + 1]
            minimum = min(minimum, board[px][py + 1])
            py += 1
        # 위
        while px > x1:
            board[px][py] = board[px - 1][py]
            minimum = min(minimum, board[px - 1][py])
            px -= 1
        # 왼쪽
        while py > y1 + 1:
            board[px][py] = board[px][py - 1]
            minimum = min(minimum, board[px][py - 1])
            py -= 1
        board[px][py] = tmp

        res.append(minimum)
    
    return res

if __name__ == '__main__':
    res = solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
    print(res)