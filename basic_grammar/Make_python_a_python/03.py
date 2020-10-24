'''
num, base = map(int, input().split())
i = 0
res = 0
while(num != 0):
    res += (num % 10) * pow(base, i)
    i += 1
    num //= 10
print(res)
'''
############################################
num = '3212'
base = 5
answer = int(num, base=5)
print(answer)