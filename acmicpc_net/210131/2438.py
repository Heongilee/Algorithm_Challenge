# 백준 2438번
# https://www.acmicpc.net/problem/2438
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    N = int(input())

    for i in range(1, N + 1):
        for j in range(i):
            print("*", end='')
        print()