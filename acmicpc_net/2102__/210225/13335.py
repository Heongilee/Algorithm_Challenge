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
            # 큐에 다음원소를 넣을 준비가 됐다면 빠져나가서 다음 원소를 계산함.
            if(weight + truck[i] <= L): break
            # 큐에 공간이 남고 다음원소를 받기에는 무게가 초과되면 0을 채워넣어 큐를 돌린다.
            Q.append(0)
            cnt += 1
        Q.append(truck[i])
        weight += truck[i]
        cnt += 1
    # 남은 차선을 계산해준다.
    cnt += w
    print(cnt)