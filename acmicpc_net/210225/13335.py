# 백준 13335번
# https://www.acmicpc.net/problem/13335
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque

if __name__ == '__main__':
    n, w, L = map(int, input().split()) # n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중
    truck = list(map(int, input().split()))
    Q = deque([])
    weight = 0
    cnt = 0

    for i in range(n):
        while True:
            if(len(Q) == w):
                weight -= Q[0]
                Q.popleft()
            if(weight + truck[i] <= L): break
            Q.append(0)
            cnt += 1
        Q.append(truck[i])
        weight += truck[i]
        cnt += 1
    cnt += w
    print(cnt)