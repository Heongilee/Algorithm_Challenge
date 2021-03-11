# 백준 2352번
# https://www.acmicpc.net/problem/2352
import sys
from bisect import bisect_left
sys.stdin = open("./acmicpc_net/input.txt", "rt")

# O(Nlog(N)) 시간 복잡도로 해결 : Lower bound
if __name__ == '__main__':
    n = int(input())
    Port = list(map(int, input().split()))
    D = [Port[0]]

    for p in Port:
        if not D or D[-1] < p:
            D.append(p)
        else:
            D[bisect_left(D, p)] = p

    print(len(D))

# O(N^2) 시간복잡도로 해결
if __name__ == '__main__':
    n = int(input())
    Port = [0] + list(map(int, input().split()))
    D = [0] * (n + 1)
    D[1] = 1

    for i in range(2, n + 1):
        if all (x > Port[i] for x in Port[1:i]):
            D[i] = 1
        else:
            D[i] = max(list(map(lambda j : D[j] if(Port[j] <= Port[i]) else 0, range(1, i)))) + 1

    print(max(D))
    