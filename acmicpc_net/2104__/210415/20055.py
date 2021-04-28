import sys
sys.stdin = open("./acmicpc_net/input.txt" ,"rt")
input = sys.stdin.readline

def rotateBelt():
    tmp = board[-1]
    for i in range(n * 2 - 1, 0, -1):
        board[i] = board[i - 1]
    board[0] = tmp

    for j in range(n - 1, 0, -1):
        if j == n - 1:
            robot[j] = False
            continue
        robot[j] = robot[j - 1]
    robot[0] = False


if __name__ == '__main__':
    n, k = map(int, input().split())
    
    board = list(map(int, input().split()))
    robot = [False] * n
    zero_cnt = 0
    res = 0
    
    while zero_cnt < k:
        rotateBelt()

        # move Robot
        for j in range(n - 2, -1, -1):
            if robot[j] and not robot[j + 1] and board[j + 1] >= 1:
                robot[j + 1] = True
                robot[j] = False
                board[j + 1] -= 1
                if board[j + 1] == 0:
                    zero_cnt += 1
        
        # insert Robot
        if board[0] != 0:
            robot[0] = True
            board[0] -= 1
            if board[0] == 0:
                zero_cnt += 1
        
        res += 1
    print(res)