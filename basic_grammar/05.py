'''
# (1)
N = int(input())

for i in range(1, N + 1):
    if(i % 2 != 0):
        print(i, end=' ')
    else:
        continue
else:
    print()
    print("정상 종료...")

# (2)
N = int(input())
sum = 0
for i in range(1, N + 1):
    sum += i
else:
    print("Total", sum)
'''
    
# (3)
N = int(input())

for i in range(1, N + 1):
    if(N % i == 0):
        print(i, end=' ')
