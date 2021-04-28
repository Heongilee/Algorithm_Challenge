# 백준 2661번
# https://www.acmicpc.net/problem/2661
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

def solve(e):
    for lt in range(len(e) - 1):
        L = 0
        while lt - L >= 0 and lt + L + 2 <= len(e):
            if e[lt - L:lt + 1] == e[lt + 1:lt + L + 2]: return False
            L += 1
    return True

def DFS(L):
    if L == n:
        if solve(numbers):
            print(''.join(map(str, numbers)))
            sys.exit(0)
    else:
        for i in range(1, 4):
            # cut edge
            if not solve(numbers + [i]): continue
            
            numbers.append(i)
            DFS(L + 1)
            numbers.pop()

if __name__ == '__main__':
    n = int(input())
    numbers = []
    DFS(0)

