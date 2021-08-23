import sys, math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    res = math.ceil(math.sqrt(n))
    print(res)
    