'''
### 이중 for문 ###
for i in range(5):
    for j in range(5):
        print("[", i,"][", j, "]", end=' ')
    print()

### 별 찍기 ###
N = int(input())
for i in range(N, 0, -1):
    for j in range(i):
        print("*", sep='', end=' ')
    print()
'''