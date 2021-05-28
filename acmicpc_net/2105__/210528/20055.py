import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    board = list(map(int, input().split()))
    robot = [False] * n
    cnt, cycle = 0, 0

    while True:
        cycle += 1

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다. 내리는 위치에 있는 로봇은 내린다.
        for i in range(n - 1, 0, -1):
            robot[i] = robot[i - 1]
        robot[0] = False
        tmp = board[2 * n - 1]
        for i in range(2 * n - 1, 0, -1):
            board[i] = board[i - 1]
        board[0] = tmp
        robot[n - 1] = False
        
        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        for i in range(n - 2, 0, -1):
            if robot[i] and board[i + 1] >= 1 and not robot[i + 1]:
                robot[i + 1] = robot[i]
                robot[i] = False
                board[i + 1] -= 1
                if board[i + 1] == 0: 
                    cnt += 1

        
        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if board[0] > 0:
            robot[0] = True
            board[0] -= 1
            if board[0] == 0:
                cnt += 1
        
        if cnt >= k: break

    print(cycle)