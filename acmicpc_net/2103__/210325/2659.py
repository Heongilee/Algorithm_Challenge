# 백준 2659번
# https://www.acmicpc.net/problem/2659
import sys
import itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
INF = int(10e3)

def clockNumber(arr):
    res = INF

    for s in range(len(arr)):
        n = 0
        for j in range(s, s + 4):
            if j >= len(arr): j %= len(arr)
            n = (n * 10) + arr[j]
        res = min(res, n)
    return res

if __name__ == '__main__':
    a = clockNumber(list(map(int, input().split())))
    res = set()

    e = list(range(1, 10))
    for mylist in list(it.product(e, e, e, e)):
        tmp = clockNumber(mylist)
        res.add(tmp)
        if tmp >= a: break
    
    print(len(res))