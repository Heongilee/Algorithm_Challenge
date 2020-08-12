import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

'''
S = input()

res = 0
for e in map(lambda x: ord(x), S):
    if(e >= 48 and e <= 57):
        n = int(chr(e))
        res = res * 10 + n
    else:
        continue

print(res)
cnt = 0
for i in range(1, res + 1):
    if(res % i == 0):
        cnt += 1

print(cnt)
'''
######################## *.isdigit()을 이용한 방법 ###############################
S = input()

res = 0
for x in S:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res + 1):
    if(res % i == 0):
        cnt += 1
print(cnt)