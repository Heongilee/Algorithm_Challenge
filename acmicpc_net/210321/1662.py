# 백준 1662번
# https://www.acmicpc.net/problem/1662
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
##################################################################
# 21/03/18 문제 DFS로 다시 풀기
#############################################################
def DFS():
    global i
    res = 0
    i += 1
    L = 0

    while i < len(t):
        if t[i].isdigit():
            L += 1
        elif t[i] == '(':
            res += L - 1 + int(t[i - 1]) * DFS()
            L = 0
        elif t[i] == ')':
            return res + L
        i += 1
    
    print(res + L)
    sys.exit(0)

if __name__ == '__main__':
    t = list(input())
    i = -1
    DFS()
