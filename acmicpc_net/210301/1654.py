# 백준 1654번
# https://www.acmicpc.net/problem/1654
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    k, n = map(int, input().split())
    line = [int(input()) for _ in range(k)]
    res = 0
    lt, rt = 1, max(line)
    
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = sum(map(lambda l: l // mid, line))

        if cnt < n:
            rt = mid - 1
        else:
            res = mid
            lt = mid + 1
    print(res)
