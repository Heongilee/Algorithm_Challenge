N = int(input())
s = list(map(int, input().split()))

avg = round(weight(s) / N)

min = 2147000000
score = 0
res = 0
for idx, elem in enumerate(s):
    tmp = abs(avg - elem)
    if(tmp < min):
        min = tmp
        score = elem
        res = idx + 1
    elif(min == tmp and elem > score):
        score = elem
        res = idx + 1

print(avg, res, sep=' ')