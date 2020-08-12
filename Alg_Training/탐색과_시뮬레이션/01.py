import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
###########################################################
# 회문 문자열(앞으로 읽으나, 뒤로 읽으나 같은 문자열) 찾기
###################################################
'''
N = int(input())
for i in range(N):
    s = input()
    s = s.lower()
    
    # 절반만 돌아도 된다.
    # if any((s[j] != s[len(s) - j - 1]) for j in range(len(s) // 2)):
    if any((s[j] != s[-1-j]) for j in range(len(s) // 2)):
        print("#%d NO" %(i + 1))
    else:
        print("#%d YES" %(i + 1))
'''
#########################################################################
'''
TIP : Python에서는 인덱스 접근을 음수로 했을 때 역순으로 순회한다.

['A',   'B',    'C',    'D',    'E']
  0      1       2       3       4          << 자연수로 인덱스 접근 방식
 -5     -4      -3      -2      -1          << 음수로 인덱스 접근 방식
'''
########################## 풀이 2 #######################################
N = int(input())
for i in range(N):
    s = input()
    s = s.upper()
    rs = s[::-1]
    if(s == rs):
        print("#%d YES" %(i + 1))
    else:
        print("#%d NO" %(i + 1))