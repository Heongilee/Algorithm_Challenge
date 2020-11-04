from collections import deque
import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
1 : 익은 토마토
0 : 익지 않은 토마토
-1 : 토마토가 없음.
'''
'''
def count_my_number(box, num):
    cnt = 0
    for e in box:
        cnt += e.count(num)
    return cnt

if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    dq = deque([])
    ans = 0

    for i in range(N):
        for j in range(M):
            if(box[i][j] == 1):
                dq.append((i, j, 0))

    # BFS
    while(dq):
        t = dq.popleft()
        ans = max(ans, t[2])

        for i in range(4):
            xx = t[0] + dx[i]
            yy = t[1] + dy[i]
            if(0 <= xx < N and 0 <= yy < M and box[xx][yy] == 0):
                box[xx][yy] = 1
                dq.append((xx, yy, t[2] + 1))

    # 안 칠한게 있다면 그건 토마토가 모두 익지 못하는 상황이다. (else)
    if((M * N) - count_my_number(box, -1) == count_my_number(box, 1)):
        print(ans)
    else:
        print(-1)
'''
##################################################################################
if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    dis = [[0] * n for _ in range(m)]
    dq = deque([])
    
    for i in range(m):
        for j in range(n):
            if(board[i][j] == 1):
                dq.append((i, j))
    
    while(dq):
        t = dq.popleft()
        
        for i in range(4):
            xx = t[0] + dx[i]
            yy = t[1] + dy[i]
            
            if(0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0):
                board[xx][yy] = 1
                dis[xx][yy] = dis[t[0]][t[1]] + 1
                dq.append((xx, yy))
                
    flag = True
    for i in range(m):
        for j in range(n):
            if(board[i][j] == 0):
                flag = False
    
    result = 0
    if(flag):
        for i in range(m):
            for j in range(n):
                if(dis[i][j] > result):
                    result = dis[i][j]
        print(result)
    else:
        print(-1)