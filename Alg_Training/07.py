import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

'''
## TIME LIMIT ERROR
N = int(input())

def isPrime(e):
    if any((e % x == 0) for x in range(2, e)):
        return False
    elif(e == 1):
        return False
    else:
        return True
        
cnt = 0
for e in range(1, N + 1):
    if(isPrime(e)):
        cnt += 1
    else:
        continue
print(cnt)
'''
########################## 에라토스테네스의 체 #####################################
'''
# prime_number_list = []
def Tot_Prime(e):
    tot = 0
    cnt = [0] * (e + 1)
    for i in range(2, e + 1):
        if(cnt[i] == 0):
            # prime_number_list.append(i)
            tot += 1
            for j in range(i, e + 1, i):
                cnt[j] += 1
    return tot

N = int(input())

print(Tot_Prime(N))
# print(prime_number_list)
'''
##################################################################################
# Sol.
N = int(input())
ch = [0] * (N + 1)
cnt = 0
for i in range(2, N + 1):
    if(ch[i] == 0):
        cnt += 1
        for j in range(i, N + 1, i):
            ch[j] = 1
print(cnt)