# 백준 1138번
# https://www.acmicpc.net/problem/1138
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    people = [-1] + list(map(int, input().split()))

    i = 1
    while i < n + 1:
        if people[i] == 0:
            people[i] = -1
            print(i, end=' ')
            for j in range(1, n + 1):
                if j < i and people[j] != -1:
                    people[j] -= 1
            i = 0
        i += 1
    print()