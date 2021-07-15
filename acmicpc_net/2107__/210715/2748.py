import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    D = [0, 1] + [0] * (int(input()) - 1)
    for i in range(2, len(D)): D[i] = D[i - 1] + D[i - 2]
    print(D[-1])
