import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

for e in b:
    a.append(e)
    
a.sort()
print(a)
'''
########################## 합병 정렬 이용 ##############################
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

c =[]

p1 = 0
p2 = 0
while(p1 < len(a) and p2 < len(b)):
    if(a[p1] < b[p2]):
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
        
if(p1 < len(a)):
    tmp = a[p1:len(a)]
else:
    tmp = b[p2:len(b)]

for e in tmp:
    c.append(e)

for e in c:
    print(e, end=' ')