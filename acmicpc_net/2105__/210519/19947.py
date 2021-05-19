import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    h, y = map(int, input().split())
    D = [h] + [0] * y
    dic = {1:1.05, 3:1.2, 5:1.35}

    for i in range(1, y + 1):
        tmp = [int(D[i - j] * dic[j]) for j in dic.keys() if i - j >= 0]
        D[i] = max([D[i]] + tmp)
    print(max(D))