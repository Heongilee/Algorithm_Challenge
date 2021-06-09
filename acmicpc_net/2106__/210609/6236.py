import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
# K원으로 몇 묶음을 만들 수 있는지?
def compare(K):
    cnt, bal = 1, 0
    for i in range(n):
        if bal + arr[i] <= K:
            bal += arr[i]
        else:
            bal = arr[i]
            cnt += 1
    return cnt

if __name__ == '__main__':
    # 1 ≤ N ≤ 100,000, 1 ≤ M ≤ N
    n, m = map(int, input().split())
    # 1 ≤ 금액 ≤ 10000
    arr = [int(input()) for _ in range(n)]
    res = None

    lt, rt = max(arr), INF
    while lt <= rt:
        mid = (lt + rt) // 2

        t = compare(mid)
        if t > m:
            lt = mid + 1
        else:
            res = mid
            rt = mid - 1
    print(res)

##########################################################################
# Python3 TLE, Pypy3 MLE
#####################################################################
'''
INF = int(10e9)
def DFS(rem):
    global result
    if len(mySize) + rem < m: return
    if len(mySize) == m - 1:
        mySize.append(rem)

        i = 0
        T = 0
        for s in mySize:
            item = 0
            for _ in range(s):
                item += arr[i]
                i += 1
            if item > T: T = item
        if T < result: result = T

        mySize.pop()
        return

    for i in range(1, n + 1):
        mySize.append(i)
        DFS(rem - i)
        mySize.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    mySize = []
    result = INF

    DFS(n)
    print(result)
'''

##########################################################################
# 18% WA
#####################################################################
'''
def compare(K):
    # K원으로 몇 묶음을 만들 수 있는지?
    cnt, bal = 1, 0
    for i in range(n):
        if bal + arr[i] <= K:
            bal += arr[i]
        else:
            bal = arr[i]
            cnt += 1
    return cnt

if __name__ == '__main__':
    # 1 ≤ N ≤ 100,000, 1 ≤ M ≤ N
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    res = None

    lt, rt = 1, 100000
    while lt <= rt:
        mid = (lt + rt) // 2

        t = compare(mid)
        if t >= m:
            if t == m: res = mid
            lt = mid + 1
        else:   # t < m (묶음을 만들 수 있는 개수가 적다는건 금액이 크다는 뜻임.)
            rt = mid - 1
    print(res)
'''