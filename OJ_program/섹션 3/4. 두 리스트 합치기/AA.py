N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

c =[]

p1 = 0
p2 = 0
while(p1 < N and p2 < M):
    if(a[p1] < b[p2]):
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
        
if(p1 < N):
    tmp = a[p1:N]
else:
    tmp = b[p2:M]

for e in tmp: 
    c.append(e)

for e in c:
    print(e, end=' ')