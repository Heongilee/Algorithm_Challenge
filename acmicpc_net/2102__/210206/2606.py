# 백준 2606번
# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

# Union-find로 풀기.
'''
def findParent(v):
    if(v != parent[v]):
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
    n = int(input()) # <= 100
    m = int(input())
    parent = list(range(n + 1))

    for _ in range(m):
        a, b = map(int, input().split())

        if(findParent(a) != findParent(b)):
            unionParent(a, b)
    print(parent)
    cnt = 0
    for i in range(1, n + 1):
        if(findParent(i) == 1):
            cnt += 1
    print(cnt - 1)
'''