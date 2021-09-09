import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    cnt = 1

    for i in range(1, n // 2 + 1):
        acc = 0
        j = i
        while acc < n:
            acc += j
            j += 1
        if acc == n:
            cnt += 1
    print(cnt)