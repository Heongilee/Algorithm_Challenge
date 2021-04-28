# 백준 2011번
# https://www.acmicpc.net/problem/2011
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
MOD = int(10e5)

if __name__ == '__main__':
    t = input()
    D = [0] * len(t)

    if int(t[0]) == 0:
        print(0)
        sys.exit(0)

    D[0] = 1
    if len(t) >= 2:
        D[1] = 2 if int(t[1]) != 0 and 0 < int(t[0:2]) <= 26 else 1
        if int(t[1]) == 0 and (int(t[0:2]) <= 0 or int(t[0:2]) > 26): D[1] = 0

        for i in range(2, len(t)):
            if int(t[i]) != 0:
                D[i] += D[i - 1]
            if int(t[i - 1]) != 0 and 0 < int(t[i - 1:i + 1]) <= 26:
                D[i] += D[i - 2]

    print(D[len(t) - 1] % MOD)
