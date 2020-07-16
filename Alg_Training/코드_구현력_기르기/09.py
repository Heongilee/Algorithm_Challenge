import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N = int(input())

max_money = 0
for n in range(N):
    a = list(map(int, input().split()))
    
    #같은거?
    s = 0
    max_elem = 0
    t = 0
    for i in range(len(a)):
        if(a[i] > max_elem):
            max_elem = a[i]
        for j in range(i + 1, len(a)):
            if(a[i] == a[j]):
                t = a[j]
                s += 1
            else:
                continue
        tmp = 0
        if(s == 0):
            tmp = max_elem * 100
        elif(s == 1):
            tmp = 1000 + t * 100
        else:
            tmp = 10000 + t * 1000
        
        if(tmp > max_money):
            max_money = tmp
            
print(max_money)
'''
###################################################################
N = int(input())

res = 0
for i in range(N):
    tmp = input().split()
    tmp.sort()
    
    a, b, c = map(int, tmp)
    if(a == b and b == c):
        money = 10000 + a * 1000
    elif(a == b or a == c):
        money = 1000 + (a * 100)
    elif(b == c):
        money = 1000 + (b * 100)
    else:
        money = c * 100
        
    if(money > res):
        res = money

print(res)