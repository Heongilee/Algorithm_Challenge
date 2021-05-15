import sys, math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
#################################################################################
# 12% WA
############################################################################
'''
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
'''
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
if __name__ == '__main__':
    # 드래곤 커브의 개수 N(1 ≤ N ≤ 20)
    N = int(input())
    board = [[0] * 110 for _ in range(110)]
    D = [list(map(int, input().split())) for _ in range(N)]

    # x, y, d, g로 이루어져 있다. 
    # (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
    for x, y, d, g in D:
        P, Q = x + dx[d], y + dy[d]
        dragon = [(x, y), (x + dx[d], y + dy[d])]
        for _ in range(g):  # g세대 만큼 반복
            L = len(dragon)
            for j in range(L):
                '''
                (X, Y)점을 점(P, Q)기준 시 90도 방향으로 회전 변환했을때 점(X', Y') 공식
                X' = -P + {X * cos(90º) - Y * sin(90º)} + P
                Y' = -Q + {X * sin(90º) + Y * cos(90º)} + Q
                '''
                x, y = dragon[j][0] - P, dragon[j][1] - Q
                xx = x * math.cos(math.radians(90)) - y * math.sin(math.radians(90))
                yy = x * math.sin(math.radians(90)) + y * math.cos(math.radians(90))
                xx, yy = int(xx + P), int(yy + Q)
                # if (xx, yy) not in dragon:
                dragon.append((xx, yy))
            P, Q = dragon[L][0], dragon[L][1]
        for x, y in dragon:
            board[y][x] = 1
    
    res = 0
    # 0 ~ 100까지의 격자라면 인덱스가 101번까지 존재하므로...
    for i in range(102):
        for j in range(102):
            if all (board[i + dx][j + dy] for dx, dy in [(0, 0), (0, 1), (1, 1), (1, 0)]):
                res += 1
    print(res)

#################################################################################
# 100% AC (80 ms)
############################################################################
'''
if __name__ == '__main__':
    N = int(input())
    board = [[0] * 101 for _ in range(101)]
    D = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for x, y, d, g in D:
        dragon = [d]
        board[y][x] = 1
        x, y = x + dx[d], y + dy[d]
        board[y][x] = 1
        for i in range(g):
            j = len(dragon) - 1
            while j >= 0:
                dragon.append((dragon[j] + 1) % 4)
                j -= 1
            if i == 0:
                dragon.pop(0)
            # paint
            for j in range(len(dragon) - 1, -1, -1):
                x, y = x + dx[dragon[j]], y + dy[dragon[j]]
                board[y][x] = 1
    
    for i in range(101):
        for j in range(101):
            if all (board[i + dx][j + dy] for dx, dy in [(0, 0), (0, 1), (1, 1), (1, 0)]):
                res += 1
    print(res)
'''
####################################################################################
# 100% AC (564 ms)
###############################################################################
'''
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
'''
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ROTATION_MATRIX = ((0,1),(-1,0))
if __name__ == '__main__':
    # 드래곤 커브의 개수 N(1 ≤ N ≤ 20)
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    dragonSet = set()

    # x, y, d, g로 이루어져 있다. 
    # (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
    for x, y, d, g in D:
        y = -y  # 좌표계 거꾸로 되어있는거 수정
        dragonList = [(x, y), (x + dx[d], y + dy[d])]
        for _ in range(g):  # g세대 만큼 반복
            P, Q = dragonList[-1][0], dragonList[-1][1]
            tmp = []
            for j in range(1, len(dragonList) + 1):
                # (X, Y)점을 점(P, Q)기준 시 90도 방향으로 회전 변환했을때 점(X', Y') 공식
                # X' = -P + {X * cos(90º) - Y * sin(90º)} + P
                # Y' = -Q + {X * sin(90º) + Y * cos(90º)} + Q
                x, y = dragonList[-j][0] - P, dragonList[-j][1] - Q
                xx = x * ROTATION_MATRIX[0][0] + y * ROTATION_MATRIX[0][1]
                yy = x * ROTATION_MATRIX[1][0] + y * ROTATION_MATRIX[1][1]
                xx, yy = xx + P, yy + Q
                tmp.append((xx, yy))
            dragonList += tmp
        dragonSet.update(dragonList)
    dragonList = list(dragonSet)
    res = 0
    for x, y in dragonList:
        if all ((x + dx, y + dy) in dragonList for dx, dy in [(1, 0), (1, -1), (0, -1)]):
            res += 1
    print(res)
