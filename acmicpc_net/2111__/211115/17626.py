import sys, itertools as it, math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
def isSquare(i):
    return True if (int(i ** 0.5) ** 2 == i) else False

if __name__ == '__main__':
    n = int(input())
    
    D = [0] * (n + 1)
    D[0], D[1] = 0, 1
    for i in range(2, n + 1):
        D[i] = 1 if isSquare(i) else i
    
    for i in range(2, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            D[i] = min(D[i], D[j * j] + D[i - j * j])
    print(D[-1])