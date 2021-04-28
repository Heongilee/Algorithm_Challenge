# 백준 2839
# https://www.acmicpc.net/problem/2839
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
################################################################################
# DP로 풀기
##########################################################################
'''
INF = int(20e9)

if __name__ == '__main__':
    N = int(input())

    D = [0] * (N + 1)
    D[3] = 1
    if(N >= 4):
        D[4] = -1
    if(N >= 5):
        D[5] = 1

    for i in range(6, N + 1):
        w3 = INF
        w5 = INF
        if(D[i - 3] != 0 and D[i - 3] != -1):
            w3 = D[i - 3]
        if(D[i - 5] != 0 and D[i - 5] != -1):
            w5 = D[i - 5]
        t = min(w3, w5)
        if(t != INF):
            D[i] = t + 1
        else:
            D[i] = -1
    print(D[N])        
'''
################################################################################
# 정석으로 풀기
##########################################################################
if __name__ == '__main__':
    N = int(input())
    res = 0

    while(N != 0):
        if(N % 5 == 0):
            res += N // 5
            break
        else:
            res += 1
            N -= 3
        
        if(N < 0):
            print(-1)
            sys.exit(0)
    print(res)