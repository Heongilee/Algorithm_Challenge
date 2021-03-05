# 백준 1725번
# https://www.acmicpc.net/problem/1725
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    N = int(input())
    height = list(int(input()) for _ in range(N))
    height.append(0)
    pt = 0
    res = 0
    S = [(pt, height[0])]    # 밑바닥 좌표값, 높이

    for i in range(1, N + 1):
        pt = i
        while S and S[-1][1] > height[i]:
            pt, h = S.pop()
            res = max(res, (i - pt) * h)
        S.append((pt, height[i]))
    print(res)