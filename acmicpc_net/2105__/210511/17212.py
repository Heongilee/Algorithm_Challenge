import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    D = [0] + [int(10e9)] * n
    for c in [1, 2, 5, 7]: 
        for i in range(c, n + 1): 
            D[i] = min(D[i], D[i - c] + 1)
    print(D[n])