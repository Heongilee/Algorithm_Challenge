import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
# 최대 일치 길이 배열(pi) 구하기
def failureFunction(string):
    pi = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
            pi[j] = j
    return pi
   
def KMP(parent, pattern):
    result = []
    lps = failureFunction(parent) # longest prefix and suffix
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = lps[j - 1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 1)
                j = lps[j]
            j += 1
    return 1 if result else 0

if __name__ == '__main__':
    S = list(input().rstrip())
    p = 0
    K = input().rstrip()
    q = 0

    # 숫자 없애기
    i = 0
    while i < len(S):
        if '0' <= S[i] <= '9': S.pop(i)
        else: i += 1
    S = "".join(S)

    # KMP 알고리즘
    print(KMP(S, K))
    

