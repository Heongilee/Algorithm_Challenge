import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    D = [1] + [0] * (n - 1)
    for i in range(1, n): D[i] = max(list(map(lambda j: D[j] if arr[j] < arr[i] else 0, range(i)))) + 1
    print(max(D))