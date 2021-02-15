# 백준 1120
# https://www.acmicpc.net/problem/1120
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    A, B = map(str, input().split())
    
    res = int(10e9)
    for i in range(len(B) - len(A) + 1):
        cnt = sum(map(lambda j : 1 if(A[j - i] != B[j]) else 0, range(i, i + len(A))))
        res = min(res, cnt)
    print(res)