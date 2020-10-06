import sys
import itertools as it # 순열이나 조합을 자동으로 구해주는 라이브러리.
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    N, F = map(int, input().split())
    b = [1] * N
    for i in range(1, N):  # 0 ~ 3
        b[i] = b[i - 1] * (N - i) // i
    a = list(range(1, N + 1))
    for tmp in it.permutations(a):
        sum = 0
        for L, x in enumerate(tmp):
            sum += (x * b[L])
        if(sum == F):
            for x in tmp:
                print(x, end=' ')
            break