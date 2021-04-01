from sys import stdin
stdin = open("./acmicpc_net/input.txt", "rt")
input = stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        D = [1] * 10
        for _ in range(int(input())):
            for i in range(1, 10): D[i] = D[i - 1] + D[i]
        print(D[-1])
