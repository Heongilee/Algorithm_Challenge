import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    r, c, w = map(int, input().split())
    D = [[1], [1, 1]]
    size = 1

    for L in range(3, r + w):
        Item = [1] * L
        for i in range(1, L - 1): Item[i] = D[-1][i - 1] + D[-1][i]
        D.append(Item)
    res, size = 0, 1
    for i in range(r - 1, r + w - 1):
        for j in range(size):
            res += D[i][c - 1 + j]
        size += 1
    print(res)