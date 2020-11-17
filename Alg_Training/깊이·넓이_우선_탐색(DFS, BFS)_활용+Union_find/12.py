import sys
import time
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
from collections import deque

'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Success
Case #05 : Success

점수 결과 : 100
time : 0.2668447495 sec
'''
'''
'''
def BFS(i, j):
    global num
    cnt = 0
    chk[i][j] = 1
    while(dq):
        t = dq.popleft()
        cnt += 1
        for i in range(4):
            xx = t[0] + dx[i]
            yy = t[1] + dy[i]
            if((0 <= xx < n) and (0 <= yy < n) and chk[xx][yy] != 1 and arr[xx][yy] == 1):
                chk[xx][yy] = 1
                dq.append((xx, yy))
    result.append(cnt)
    return
    

if __name__ == "__main__":
    start_time = time.time()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]   #행렬 인풋이 붙어있기 때문에 .split() 사용 안함.
    result = [-1]
    num = 0
    chk = [[0] * n for _ in range(n)]
    dq = deque([])
    
    for i in range(n):
        for j in range(n):
            if(chk[i][j] != 1 and arr[i][j] == 1):
                dq.append((i, j))
                BFS(i, j)
                
    result = sorted(result[1:])
    # Output
    print(len(result))
    for i in range(len(result)):
        print(result[i])
    end_time = time.time()
    print(f"time : {round(end_time-start_time, 10)} sec")
################################################################################################
'''
time : 0.1700778008 sec
'''
'''
def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1):
            DFS(xx, yy)
    

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for i in range(len(res)):
        print(res[i])
'''