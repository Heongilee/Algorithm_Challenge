import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
# 80점... (4번 문제)
A = dict()
B = dict()

for i in range(2):
    t = input()
    if(i == 0):
        for c in t:
            if(A.get(t) == None):
                A[c] = 1
            else:
                A[c] += 1
    else:
        for c in t:
            if(B.get(t) == None):
                B[c] = 1
            else:
                B[c] += 1

for K, V in A.items():
    if(A.get(K) == B.get(K)):
        continue
    else:
        print("NO")
        break
else:
    for K, V in B.items():
        if(B.get(K) == A.get(K)):
            continue
        else:
            print("NO")
            break
    else:
        print("YES")
'''
###########################################################################
# dict().get(K, default) : 딕셔너리의 키값을 반환하고 없다면 default를 반환시킴.
'''
A = input()
B = input()
str1 = dict()
str2 = dict()

for x in A:
    str1[x] = str1.get(x, 0) + 1
for y in B:
    str2[y] = str2.get(y, 0) + 1

for K in str1.keys():   #str1 딕셔너리의 키값들만 방문하고 싶다.
    if (K in str2.keys()) and (str1.get(K) == str2.get(K)):
        continue
    else:
        print("NO")
        break
else:
    print("YES")
'''
####################### <개선 버전> #########################################
'''
A = input()
B = input()
H = dict()

# A에는 있고 B에는 없는 문자의 경우, 1
# A와 B 둘다 있는 문자의 경우, 0
# A에는 없고 B에는 있는 문자의 경우, -1
for x in A:
    H[x] = H.get(x, 0) + 1
for x in B:
    H[x] = H.get(x, 0) - 1

if any (H.get(x) != 0 for x in H.keys()):
    print("NO")
else:
    print("YES")
'''
###############################################################################
# List Hashing 방식 (C++로 풀 듯이 접근.)
A = input()
B = input()
str1 = [0] * 52
str2 = [0] * 52

def upperindexOf(i):
    return i - 65
def lowerindexOf(i):
    return i - 71

for x in A:
    if x.isupper():
        str1[upperindexOf(ord(x))] += 1
    else:
        str1[lowerindexOf(ord(x))] += 1

for y in B:
    if y.isupper():
        str2[upperindexOf(ord(y))] += 1
    else:
        str2[lowerindexOf(ord(y))] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
    else:
        continue
else:
    print("YES")