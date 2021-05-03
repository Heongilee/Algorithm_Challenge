import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

'''
에라토스테네스의 체?
-> 소수를 빠르게 구하는 방법.

'''
# 시간 복잡도 : O(n)
# def isPrime(n):
#     return False if any (n % i == 0 for i in range(2, n)) else True

# 시간 복잡도 : O(n^(1/2))
import math
def isPrime(n):
    return False if any (n % i == 0 for i in range(2, int(math.sqrt(n)) + 1)) else True

# 에라토스테네스의 체
def primeSieve(n):
    arr = [True] * (n + 1)

    m = int(n ** 0.5)   # math 라이브러리 없이 제곱근 구하는 방법.
    for i in range(2, m + 1):
        if not arr[i]: continue
        for j in range(i + i, n + 1, i):
            arr[j] = False

    return [i for i in range(2, n + 1) if arr[i]]

if __name__ == '__main__':
    n = int(input())
    myList = primeSieve(n)
    cnt = 0
    for lt in range(len(myList)):
        rt = lt
        tot = 0
        while rt < len(myList) and tot < n:
            tot += myList[rt]
            rt += 1
        if tot == n: cnt += 1
    print(cnt)