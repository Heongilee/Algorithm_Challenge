import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))   # 1 <= arr[i] <= 1,000
    board = [None] + list(map(lambda i: True if i in arr else False, range(1, max(arr) + 1)))

    i = 0
    tape = 0
    while i < len(board):
        if not board[i]:
            i += 1
            continue
        else:
            for j in range(i, i + l): 
                if j >= len(board): break
                board[j] = False
            tape += 1
            i += l
    print(tape)


######################################################################################################################
# 5% WA
# 
# 반례
# 6 5
# 1 4 5 6 7 10
# answer is 2
# output is 3
#################################################################################################################
'''
if __name__ == '__main__':
    # 1 <= n, l <= 1,000
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))   # 1 <= arr[i] <= 1,000
    board = [None] + list(map(lambda i: True if i in arr else False, range(1, max(arr) + 1)))

    trueCnt = board.count(True)    # board 리스트에 False가 전부 사라지면, while문을 빠져 나옴.
    tape = 0

    while True:
        # 가장 많은 구멍(hole)을 포함하는 테이프 위치 왼쪽(Mlt)과 오른쪽(Mrt)
        Mlt, Mrt = None, None
        hole = 0

        # 슬라이딩 윈도우
        lt = 1
        rt = lt + l
        maxV = hole = board[lt:rt].count(True)
        Mlt, Mrt = lt, rt
        
        while True:
            rt += 1
            if rt >= len(board) + 1: break  # escape condition
            if board[rt - 1]: hole += 1
            lt += 1
            if board[lt - 1]: hole -= 1

            if hole > maxV:
                maxV = hole
                Mlt, Mrt = lt, rt

        # 테이프 붙임
        for i in range(Mlt, Mrt):
            if i >= len(board): break
            if board[i]:
                board[i] = False
                trueCnt -= 1

        tape += 1
        if not trueCnt:
            print(tape)
            sys.exit(0)
'''