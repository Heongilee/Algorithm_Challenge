# 백준 11339번
# https://www.acmicpc.net/problem/11399
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    pq = list(map(int, input().split()))

    pq.sort()
    res = weight(list(map(lambda i : weight(pq[:i]), range(1, n + 1))))
    print(res)
