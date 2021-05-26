import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

##################################################################
# 입력 데이터 1,000,000
#############################################################
'''
if __name__ == '__main__':
    N = int(input())
    board = [1000000] * N
    B, C = map(int, input().split())
    res = N

    for i in range(N):
        board[i] -= B

        if board[i] < 0: continue
        div, mod = divmod(board[i], C)
        res += div
        if mod > 0:
            res += 1

    print(res)
'''
if __name__ == '__main__':
    N = int(input())
    board = list(map(int, input().split()))
    B, C = map(int, input().split())
    res = N

    for i in range(N):
        board[i] -= B
        if board[i] < 0: continue
        div, mod = divmod(board[i], C)
        res += div + 1 if mod > 0 else div

    print(res)
