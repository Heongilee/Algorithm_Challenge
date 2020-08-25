import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

'''
쇠막대기와 
레이저의 배치를 나타내는 괄호 표현이 주어졌을 때,

쇠막대기 조각의 총 개수는?

-> 닫는 괄호를 만났을 때 빼내고 현재 높이 값 출력.
'''
# 20점...
'''
a = list(map(str, input()))
S = []

cnt = 0
for i in range(len(a)):
    if(a[i] == '('):
        S.append('(')
    elif(a[i] == ')'):
        S.pop()
        if(a[i - 1] == ')'):
            cnt += 1
        else:
            cnt += len(S)
print(cnt)
'''
##############################################################################
# Solution...

s = input()
S = []
cnt = 0
for i in range(len(s)):
    if(s[i] == '('):
        S.append(s[i])
    else:
        S.pop()
        if(s[i - 1] == '('):
            cnt += len(S)
        else:
            cnt += 1
print(cnt)