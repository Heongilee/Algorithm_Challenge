import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    t = n = int(input())

    cycle = 0
    while True:
        T = str(t)
        if 0 <= t <= 9:
            T = "0" + T[-1]
        res = int(T[0]) + int(T[1])
        Res = str(res)
        T = T[1] + Res[-1]
        t = int(T)
        cycle += 1
        if t == n: break
    print(cycle)