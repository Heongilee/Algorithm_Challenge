# 백준 15729번
# https://www.acmicpc.net/problem/15729
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    board = list(map(int, input().split()))
    my = [0] * n
    res = 0

    while True:
        for i in range(n):
            if my[i] == board[i]: continue
            else:
                res += 1
                for j in range(i, i + 3):
                    if j > n - 1: 
                        break
                    my[j] = 1 - my[j]
        else:
            print(res)
            sys.exit(0)