import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
def reverse(x):
    itos = str(x)
    stoi = ""
    for i in range(len(itos) - 1, -1, -1):
        stoi += itos[i]
    return int(stoi)

# # 자릿수 바꾸는 테크닉 알아둘 것!!
# def reverse_1(x):
#     # x = 9010 -> 0109
#     res = 0
#     while(x > 0):
#         t = x % 10
#         res = res * 10  + t
#         x //= 10
#     return res
    

def isPrime(x):
    if(x == 1):
        return False
    cnt = [0] * (x + 1)
    for i in range(2, x):
        if(cnt[i] == 0):
            for j in range(i, x + 1, i):
                if(j == x):
                    return False
                cnt[j] = 1
    else:
        return True

N = int(input())
a = list(map(int, input().split()))

for e in a:
    r = reverse_1(e)
    # r = reverse(e)
    if(isPrime(r)):
        print(r, end=' ')
'''
#######################################################################
import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")


# 자릿수 바꾸는 테크닉 알아둘 것!!
def reverse_1(x):
    # x = 9010 -> 0109
    res = 0
    while(x > 0):
        t = x % 10
        res = res * 10  + t
        x //= 10
    return res
    
def isPrime_1(x):
    if(x == 1):
        return False
    # 1 * 16 = 16
    # 2 * 8 = 16
    # 따라서, 넘어온 값의 절반만 순회해서 검사해도 된다.
    for i in range(2, x // 2 + 1):
        if(x % i == 0):
            return False
    else:
        return True
        
N = int(input())
a = list(map(int, input().split()))

for e in a:
    r = reverse_1(e)
    # r = reverse(e)
    # if(isPrime(r)):
    if(isPrime_1(r)):
        print(r, end=' ')