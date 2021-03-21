# 백준 1662번
# https://www.acmicpc.net/problem/1662
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
#######################################################################
# 내 풀이 
##################################################################
'''
def DFS(string):
    cnt = 0
    
    i = len(string)
    while i >= 0:
        if string[i] == '(':
            break
        elif string[i] == ')':
            a, b = DFS(string[:i - 1])  # 괄호 안에 있는 개수
            i = a
            cnt += (string[i] - '0') * b
            # cnt += (string[i] - 1) * b
        else:
            cnt += 1
        i -= 1
    
    return i - 1, cnt

if __name__ == '__main__':
    t = DFS(input())
    print(t[1])
'''
    
    
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