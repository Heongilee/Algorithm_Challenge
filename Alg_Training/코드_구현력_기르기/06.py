import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

'''
def digit_sum(x):
    cnt = 0
    dec = 1
    while(x // dec != 0):
        cnt += ((x % (dec * 10)) - (x % dec)) // dec
        dec *= 10
    return cnt

N = int(input())
a = list(map(int, input().split()))

max_cnt = -2147000000
max_val = a[0]
for e in a:
    cnt = digit_sum(e)
    if(cnt > max_cnt):
        max_cnt = cnt
        max_val = e
        
print(max_val)
'''
##################################################################
# 각 자릿수 구하기  -> 풀이 1
# sum += number % dec
# number /= 10 
###########################
'''
N = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while(x > 0):
        sum += x % 10
        x //= 10
    return sum

max_tot = -2147000000
res = a[0]
for x in a:
    tot = digit_sum(x)
    if(tot > max_tot):
        max_tot = tot
        res = x

print(res)
'''
############################ 풀이 2 ####################################
N = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    # x 정수값을 string으로 타입 캐스팅해서 문자 하나하나를 처리함. -> Python이니까 가능한 것.
    for i in str(x):
        sum += int(i)
    return sum
        

max_tot = -2147000000
res = a[0]
for x in a:
    tot = digit_sum(x)
    if(tot > max_tot):
        max_tot = tot
        res = x

print(res)