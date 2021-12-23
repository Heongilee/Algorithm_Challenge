import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    g = gcd(numbers[0], gcd(numbers[1], numbers[-1]))
    
    print(f"gcd is {g}")
    #* 왜 최대공약수의 반만 검사해도 되는걸까?
    for i in range(1, (g // 2) + 1):
        if g % i == 0:
            print(i)
    print(g)
    
'''
# 정석
if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split())) # numbers[i] <= 10e7

    for t in range(1, min(numbers) + 1):
        for nn in numbers:
            if nn % t != 0:
                break
        else:
            print(t)
'''