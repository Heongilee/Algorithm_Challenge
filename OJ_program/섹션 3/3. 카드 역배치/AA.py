a = list(range(0, 21))
N = 10

def swap(x, y):
    tmp = x
    x = y
    y = tmp
    
    return x, y

for n in range(N):
    ai, bi = map(int, input().split())
    
    for i in range((abs(bi-ai) + 1) // 2):
        a[ai + i], a[bi - i] = swap(a[ai + i], a[bi - i])

# # 1번째 방법
# for i in range(1, len(a)):
#     print(a[i], end=' ')
    
# 2번째 방법
a.pop(0)
for elem in a:
    print(elem, end=' ')