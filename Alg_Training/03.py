import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
'''
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
###########################################################################
# TIP : Python에서 swap 사용법

'''
a = 10
b = 20

a, b = b, a
print(a, b)
'''
###########################################################################
# for문이 돌면서 변수에 할당받지 않고 그냥 반복만 하고 싶을 때?

'''
for _ in range(10):
    # 변수에 할당하지 않고 10번 반복만 시켜준다.
'''
###########################################################################