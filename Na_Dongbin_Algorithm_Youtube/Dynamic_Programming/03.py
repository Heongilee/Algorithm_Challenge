import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    n, m = map(int, input().split())
    coin = list(int(input()) for _ in range(n))
    D = [2147000000] * (m + 1)
    D[0] = 0

    for c in coin:
        for i in range(c, m + 1):
            D[i] = min(D[i], D[i - c] + 1)
        print(D)
    print(D)
