import sys
from math import factorial
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        print(factorial(m) // (factorial(n) * factorial(m - n)))