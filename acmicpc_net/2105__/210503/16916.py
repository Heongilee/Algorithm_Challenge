import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 실패 함수를 이용하여 접두사와 접미사가 같은 최대 길이 배열(pi) 구하기
def failureFunction(string):
    m = len(string)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and string[i] != string[j]:
            # 이전에 일치했던 부분까지 돌아가서 다시 검사 수행.
            j = pi[j - 1]   
        if string[i] == string[j]:
            j += 1
            pi[i] = j
    return pi

def KMP(string, pattern):
    isExist = False
    pi = failureFunction(string)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = pi[j - 1]
        if string[i] == pattern[j]:
            # j가 m - 1위치에 있다는 말은 pattern문자열을 모두 일치했다는 뜻이므로 부분 문자열을 찾은 것이다.
            if j == len(pattern) - 1:
                isExist = True
                # 이전에 일치했던 부분 문자열의 접두사 위치로 이동한다.
                j = pi[j]
            else:
                j += 1
    
    return 1 if isExist else 0

S, P = tuple(input().rstrip() for _ in range(2))
print(KMP(S, P))