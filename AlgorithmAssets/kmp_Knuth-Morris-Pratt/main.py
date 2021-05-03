'''
KMP(Knuth-Morris-Pratt)알고리즘
단순 문자열 비교의 경우 O(n * m)시간이 걸릴 수 있다.
e.g. )길이가 10,000,000인 글에서 길이가 1,000인 부분 문자열을 찾을 때, 연산 양이 100억에 달한다.

KMP 알고리즘을 이용하면 O(n + m)시간에 구할 수 있다.
'''
import sys
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

def KMP(parent, pattern):
    foundIndex = []
    pi = buildPiTable(parent)
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = pi[j - 1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                foundIndex.append(i - len(pattern) + 1)
                # print(i - len(pattern) + 2, "번째에서 찾았습니다.", end=' ')
                j = pi[j]
            j += 1
    
    return foundIndex if foundIndex else ["발견하지못함"]

if __name__ == '__main__':
    print(' '.join(map(str, KMP("ababacabacaabacaaba", "abacaaba"))))
    print(' '.join(map(str, KMP("baekjoon", "aek"))))
    print(' '.join(map(str, KMP("baekjoon", "bak"))))
    print(' '.join(map(str, KMP("baekjoon", "joo"))))
    print(' '.join(map(str, KMP("baekjoon", "oone"))))
    print(' '.join(map(str, KMP("baekjoon", "online"))))
    print(' '.join(map(str, KMP("baekjoon", "baekjoon"))))