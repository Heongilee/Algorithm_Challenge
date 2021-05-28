import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
##################################################################
# AC, Parametric Search를 이용한 방법.
#
# https://www.notion.so/Binary-Search-Parametric-Search-c49e78dc5f9e448e8047efb5502c8e28
#############################################################

def compare(mid):
    cnt = 0
    S = 0
    for i in range(n):
        S += board[i]
        if S >= mid:
            S = 0
            cnt += 1
    return cnt

if __name__ == '__main__':
    n, k = map(int, input().split())
    board = list(map(int, input().split()))
    lt = 0
    rt = sum(board) #총 합을 최댓값으로 설정.

    while lt <= rt:
        cnt = 0
        S = 0
        mid = (lt + rt) // 2
        cnt = compare(mid)
        
        if cnt >= k:
            lt = mid + 1
        else:
            rt = mid - 1
    print(rt)

##################################################################
# 1% TLE
#############################################################
'''
sys.setrecursionlimit(10 ** 6)
INF = int(10e9)
def DFS(L, rem):
    global res
    if L == k - 1:
        if rem <= 0: return
        size.append(rem)

        tmp = INF
        lt, rt = 0, 0
        for s in size:
            rt += s
            tot = sum(board[lt:rt])
            if tot < tmp: tmp = tot
            lt = rt
            
        if tmp > res: res = tmp
        size.pop()
        return

    for i in range(1, n):
        size.append(i)
        DFS(L + 1, rem - i)
        size.pop()

if __name__ == '__main__':
    n, k = map(int, input().split())
    board = list(map(int, input().split()))
    size = []
    res = -1

    DFS(0, n)
    print(res)
'''