# 백준 1662번
# https://www.acmicpc.net/problem/1662
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
INF = int(10e3) + 1
if __name__ == '__main__':
    N = int(input())
    cnt = [0] * INF

    for _ in range(N):
        t = int(sys.stdin.readline())
        cnt[t] += 1

    
    for i in range(INF):
        if cnt[i] != 0:
            for j in range(cnt[i]):
                print(i)