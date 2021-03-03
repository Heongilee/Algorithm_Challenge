# 백준 17609번
# https://www.acmicpc.net/problem/17609
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
########################################################################
# 내 풀이
#
# pop 메서드 쓰기보다 투 포인터 쓰는게 나아보임...
###################################################################
'''
def palindrome(t):
    t = deque(t)
    while t:
        if t[0] == t[-1]:
            t.pop()
            if t:
                t.popleft()
        else:
            return False
    return True

def solution(t):
    t = deque(t)
    while t:
        if t[0] == t[-1]:
            t.pop()
            if t:
                t.popleft()
        else:
            T = ''.join(t)
            if T[:len(T) - 1][0] == T[:len(T) - 1][-1]:
                t.pop()
                T = T[:len(T) - 1]
            elif T[1:][0] == T[1:][-1]:
                t.popleft()
                T = T[1:]
            res = palindrome(T)
            return 1 if res else 2

    return 0

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        t = input()
        print(solution(t))
'''
###########################################################################
# 다른 사람 풀이
######################################################################
def isPalindrome(text, lt, rt):
    if(len(text) == 1):
        return True
    while lt < rt:
        if text[lt] == text[rt]:
            lt += 1
            rt -= 1
        else:
            return False
    return True
        
def solution(text, lt, rt):
    if(len(text) == 1):
        return 0
    while lt < rt:
        if text[lt] == text[rt]:
            lt += 1
            rt -= 1
        else:
            if isPalindrome(text, lt + 1, rt) or isPalindrome(text, lt, rt - 1):
                return 1
            else:
                return 2
    return 0

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        text = input()
        print(solution(list(text), 0, len(text) - 1))