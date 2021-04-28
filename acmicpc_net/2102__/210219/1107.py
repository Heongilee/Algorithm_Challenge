# 백준 1107번
# https://www.acmicpc.net/problem/1107
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    nums = []
    if(M > 0):        
        nums = list(map(str, input().split()))
    pos = 100
    res = abs(N - pos)

    for i in range(1000001):
        t = list(str(i))
        if all (n not in t for n in nums): # 조건에 맞는 숫자임.
            res = min(res, len(t) + abs(N - i))

    print(res)