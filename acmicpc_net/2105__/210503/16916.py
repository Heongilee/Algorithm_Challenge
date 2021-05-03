import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 최대 일치 길이 배열(pi) 구하기
def buildPiTable(string):
    m = len(string)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]   # 이전에 일치했던 부분까지 돌아가서 다시 검사를 수행할 것.
        if string[i] == string[j]:
            j += 1
            pi[i] = j
    return pi

def KMP(string, pattern):
    isExist = False
    pi = buildPiTable(string)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = pi[j - 1]
        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                isExist = True
                j = pi[j]
            else:
                j += 1
    
    return 1 if isExist else 0

S, P = tuple(input().rstrip() for _ in range(2))
print(KMP(S, P))