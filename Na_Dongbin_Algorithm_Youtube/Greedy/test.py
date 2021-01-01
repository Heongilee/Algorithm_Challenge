import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt")

if __name__ == "__main__":
    N, K = map(int, input().split())
    cnt = 0

    while True:
        t = (N // K) * K
        cnt += N - t
        N = t

        if(N < K):
            break

        cnt += 1
        N //= K
    print(cnt)

        