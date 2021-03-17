# 백준 13913번
# https://www.acmicpc.net/problem/13913
#########################################################################
# 답안
####################################################################
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
SIZE = int(10e4) + 1

def BFS(n):
    dq = deque()
    dq.append(n)

    while dq:
        t = dq.popleft()
        if t == m:
            print(dis[t])
            arr = []
            while t != n:
                arr.append(t)
                t = prev[t]
            arr.append(n)
            print(' '.join(map(str, arr[::-1])))
            return
        for tt in (t - 1, t + 1, t * 2):
            if 0 <= tt < SIZE and not dis[tt]:
                dis[tt] = dis[t] + 1
                prev[tt] = t
                dq.append(tt)

if __name__ == '__main__':
    n, m = map(int, input().split())
    dis = [0] * SIZE    # 거리를 기록
    prev = [-1] * SIZE   # 이전 노드를 기록

    BFS(n)

#########################################################################
# 내 풀이 (BOJ 70% WA)
####################################################################
'''
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
SIZE = int(10e4) + 1

def pathExpression(path, d):
    arr = []
    while d != n:
        arr.append(d)
        d = prev[d]
    for e in [n] + arr[::-1]:
        print(e, end=' ')

def BFS(n):
    dq = deque()
    dq.append((n, n - 1))
    dq.append((n, n + 1))
    dq.append((n, n * 2))

    while dq:
        a, b = dq.popleft()

        if 0 <= b < SIZE and dis[b] == 0:
            dis[b] = dis[a] + 1
            prev[b] = a

            if b == m:
                print(dis[b])
                # print(path[:25])
                pathExpression(prev, m)
                print()

            dq.append((b, b - 1))
            dq.append((b, b + 1))
            dq.append((b, b * 2))


if __name__ == '__main__':
    n, m = map(int, input().split())
    dq = deque()
    # SIZE = max(n, m) * 2 + 1
    dis = [0] * SIZE    # 거리를 기록
    prev = [0] * SIZE   # 이전 노드를 기록

    BFS(n)
'''