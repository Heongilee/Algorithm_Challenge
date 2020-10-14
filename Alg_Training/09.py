import sys
from collections import deque
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Success
Case #05 : Success

점수 결과 : 100
'''
'''
if __name__ == '__main__':
    dx = [-1, 0, +1, 0]
    dy = [0, +1, 0, -1]
    N = 7
    M = list(list(map(int, input().split())) for _ in range(N))
    visit = list([0] * N for _ in range(N))
    
    # 벽 만들기
    for m in M:
        m.insert(0, 1)
        m.append(1)
    M.insert(0, [1, 1, 1, 1, 1, 1, 1, 1, 1])
    M.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
    start = (1, 1)
    end = (7, 7)
    
    dQ = deque([])
    dQ.append(start)
    L = 0
    while dQ:
        size = len(dQ)
        for _ in range(size):
            t = dQ.popleft()
            if((t[0], t[1]) == end):
                print(L)
                exit(0)
            visit[t[0] - 1][t[1] - 1] = 1
            if((t[0], t[1]) == end):
                break
            for i in range(4):
                if(M[t[0] + dx[i]][t[1] + dy[i]] != 1 and visit[t[0] + dx[i] - 1][t[1] + dy[i] - 1] != 1):
                    dQ.append((t[0] + dx[i], t[1] + dy[i]))
        L += 1
    print(-1)
'''
####################################################################################
if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    board = list(list(map(int, input().split())) for _ in range(7))
    dis = [[0] * 7 for _ in range(7)]
    dQ = deque()
    dQ.append((0, 0))
    board[0][0] = 1
    while dQ:
        tmp = dQ.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if(0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0):
                board[x][y] = 1
                dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                dQ.append((x, y))
    if(dis[6][6] == 0):
        print(-1)
    else:
        print(dis[6][6])