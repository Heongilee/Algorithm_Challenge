# https://www.acmicpc.net/problem/11047
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == "__main__":
    n, k = map(int, input().split())
    coin = []
    cnt = 0

    for i in range(n):
        c = int(input())
        coin.append(c)
    
    coin.sort(reverse=True)
    for i in range(n):
        if(k // coin[i] == 0):
            continue
        else:
            cnt += k // coin[i]
            k %= coin[i]
    print(cnt)