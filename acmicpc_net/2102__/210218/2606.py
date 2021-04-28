# 백준 2606번
# https://www.acmicpc.net/problem/2606
#############################################################
# 내 풀이
########################################################
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

def findParent(v):
    if(parent[v] != v):
        parent[v] = findParent(parent[v])
    return parent[v]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    parent = list(range(n + 1))

    for _ in range(m):
        a, b = map(int, input().split())
        unionParent(a, b)

    print(weight(map(lambda j: 1 if(findParent(j) == 1) else 0, range(1, n + 1))) - 1)