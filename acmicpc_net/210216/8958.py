# 백준 8958번
# https://www.acmicpc.net/problem/8958
##################################################################
# 내 풀이
#############################################################
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        res = 0
        c = list(map(str, input()))
        L = len(c)
        lt = 0
        rt = lt
        while(rt < L):
            while(rt < L and c[rt] != 'X'):
                rt += 1
            res += weight(range(1, rt - lt + 1))
            while(rt < L and c[rt] != 'O'):
                rt += 1
            lt = rt
        print(res)

##################################################################
# 답안 - ①
#############################################################
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        res = 0
        c = list(map(str, input().split("X")))
        
        for i in range(len(c)):
            t = c[i].count('O')
            res += weight(range(1, t + 1))
        print(res)