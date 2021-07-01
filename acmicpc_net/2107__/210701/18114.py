import sys
import itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e7)
if __name__ == '__main__':
    n, c = map(int, input().split())
    items = list(map(int, input().split()))
    chk = [0] * (INF + 1)
    for i in items: chk[i] = 1

    if chk[c]:
        print(1)
        sys.exit(0)
    for X in it.combinations(items, 2):
        t = sum(X)
        if t == c:
            print(1)
            sys.exit(0)
        elif t < c:
            if chk[c - t] and (c - t not in X):
                print(1)
                sys.exit(0)
    print(0)

#########################################################################################
# DP -> Python 0% TLE, Pypy 8% TLE
#
# 또한, 최대 3개 선택해야 한다는 조건에 위배된다.
####################################################################################
'''
if __name__ == '__main__':
    n, c = map(int, input().split())
    D = [0] * (c + 1)

    D[0] = 1
    myList = sorted(list(map(int, input().split())))
    for i in range(c, 0, -1):   # c가 최대 10^8 이므로 O(n)은 시간 초과가 생길 수 있다.
        for e in myList:
            if i - e < 0: break
            D[i] = 1 if D[i - e] else D[i]

            if D[c]:
                print(1)
                sys.exit(0)
    
    print(1 if D[c] else 0)
'''
