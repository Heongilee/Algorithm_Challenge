import sys
sys.setrecursionlimit(10 ** 6)

# 최대값을 가진 영역 색칠하기    
def boardPainting(h_lt, h_rt, v_lt, v_rt):
    for i in range(v_lt, v_rt + 1):
        for j in range(h_lt, h_rt + 1):
            visited[i][j] = True

# visited 테이블에 True가 한개 있으면 True 아니면 False
def oneTrueInVisited():
    flag = False
    for i in range(n):
        for j in range(n):
            if flag and visited[i][j]:
                return False
            elif visited[i][j]:
                flag = True
    return flag

# 보드의 최댓값 위치 찾기
def maximumValuePositionInBoard(board, M, h_lt, h_rt, v_lt, v_rt):
    Mpos = []
    for i in range(v_lt, v_rt + 1):
        for j in range(h_lt, h_rt + 1):
            if board[i][j] == M and not visited[i][j]:
                Mpos.append((i, j))
    
    return Mpos

# 보드의 최댓값 찾기
def maximumValueInBoard(board, h_lt, h_rt, v_lt, v_rt):
    M = 0
    for i in range(v_lt, v_rt + 1):
        for j in range(h_lt, h_rt + 1):
            if board[i][j] > M and not visited[i][j]:
                M = board[i][j]
    
    return M

# 방문 안한 영역이 1개 남을때 까지 DFS 탐색.
def DFS(h_lt, h_rt, v_lt, v_rt):
    global cost
    if oneTrueInVisited():
        return
    
    M = maximumValueInBoard(board, h_lt, h_rt, v_lt, v_rt)
    cost += M
    Mpos = maximumValuePositionInBoard(board, M, h_lt, h_rt, v_lt, v_rt)

    lt, rt = h_lt, h_rt
    mid = (lt + rt) // 2    # 4 // 2 = 2 (lt, mid)(mid + 1, rt)
    for x, y in Mpos:
        if 0 <= x <= mid:
            if 0 <= y <= mid:   #1 사분면
                boardPainting(0, mid, 0, mid)
                DFS(0, mid, 0, mid)
            elif mid + 1 <= y <= rt:    #2 사분면 
                boardPainting(mid + 1, rt, 0, mid)
                DFS(mid + 1, rt, 0, mid)
        elif mid + 1 <= x <= rt:
            if 0 <= y <= mid:   #3 사분면
                boardPainting(0, mid, mid + 1, rt)
                DFS(0, mid, mid + 1, rt)
            elif mid + 1 <= y <= rt:    #4 사분면
                boardPainting(mid + 1, rt, mid + 1, rt)
                DFS(mid + 1, rt, mid + 1, rt)

    lt, rt = v_lt, v_rt
    mid = (lt + rt) // 2    # 4 // 2 = 2 (lt, mid)(mid + 1, rt)
    for x, y in Mpos:
        if 0 <= x <= mid:
            if 0 <= y <= mid:   #1 사분면
                boardPainting(0, mid, 0, mid)
                DFS(0, mid, 0, mid)
            elif mid + 1 <= y <= rt:    #2 사분면
                boardPainting(mid + 1, rt, 0, mid)
                DFS(mid + 1, rt, 0, mid)
        elif mid + 1 <= x <= rt:
            if 0 <= y <= mid:   #3 사분면
                boardPainting(0, mid, mid + 1, rt)
                DFS(0, mid, mid + 1, rt)
            elif mid + 1 <= y <= rt:    #4 사분면
                boardPainting(mid + 1, rt, mid + 1, rt)
                DFS(mid + 1, rt, mid + 1, rt)

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    cost = 0

    M = maximumValueInBoard(board, 0, n - 1, 0, n - 1)
    cost += M
    Mpos = maximumValuePositionInBoard(board, M, 0, n - 1, 0, n - 1)
    
    lt, rt = 0, n - 1
    mid = (lt + rt) // 2    # 4 // 2 = 2 (lt, mid)(mid + 1, rt)

    for x, y in Mpos:
        if 0 <= x <= mid:
            if 0 <= y <= mid:   #1 사분면
                boardPainting(0, mid, 0, mid)
                DFS(0, mid, 0, mid)
            elif mid + 1 <= y <= rt:    #2 사분면
                boardPainting(mid + 1, rt, 0, mid)
                DFS(mid + 1, rt, 0, mid)
        elif mid + 1 <= x <= rt:
            if 0 <= y <= mid:   #3 사분면
                boardPainting(0, mid, mid + 1, rt)
                DFS(0, mid, mid + 1, rt)
            elif mid + 1 <= y <= rt:    #4 사분면
                boardPainting(mid + 1, rt, mid + 1, rt)
                DFS(mid + 1, rt, mid + 1, rt)
    
    print(cost)