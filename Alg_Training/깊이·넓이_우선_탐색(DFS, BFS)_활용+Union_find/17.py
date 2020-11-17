import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

def DFS(L, S):
    global res
    if(L == M):
        cnt = 0
        for x1, y1 in hs:
            minimum = 2147000000
            for x2, y2 in sack:
                dis = abs(x2 - x1) + abs(y2 - y1)
                
                # 현재 집에서 피자배달거리가 최소인 피자집 거리를 minimum에 저장.
                minimum = min(dis, minimum)
            # 각 피자집들의 최소 피자배달거리들을 모두 더함.
            cnt += minimum
        # 현재 조합과 이전 조합을 비교했을 때 최소 거리합이 최소인 값을 res에 저장.
        res = min(cnt, res)
        return
    else:
        for i in range(S, len(pz)):
            sack.append(pz[i])
            DFS(L + 1, i + 1)
            sack.pop()

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split() )) for _ in range(N)]
    sack = []
    pz = []
    hs = []
    res = 2147000000
    
    for i in range(N):
        for j in range(N):
            if(board[i][j] == 1):
                hs.append((i, j))
            elif(board[i][j] == 2):
                pz.append((i, j))
    
    DFS(0, 0)
    print(res)