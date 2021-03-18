# 백준 1662번
# https://www.acmicpc.net/problem/1662
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
#######################################################################
# 내 풀이 WA
##################################################################
def DFS(string):
    global L
    for i in range(len(string)):
        if string[i].isdigit():
            L += 1
            tmp = string[i]
        elif string[i] == '(':
            j = i
            while j < len(string):
                if j == ')':
                    break
                j += 1
            DFS(string[i + 1:j])
        else:
            pass
##################################################################
# 다른 사람 풀이
#############################################################            
if __name__ == '__main__':
    S = []
    L = 0
    tmp = ''
    for e in input():
        if e.isdigit():
            L += 1
            tmp = e
        elif e == '(':
            S.append((tmp, L - 1))
            L = 0
        else:
            a, b = S.pop()

            L = (int(a) * L) + b
    print(L)
    