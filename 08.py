import random as rd

'''
### 빈 리스트 생성 ###
empty_list_1 = [] #빈 리스트 생성 (1)
empty_list_2 = list() #빈 리스트 생성 (1)

print(empty_list_1)
print(empty_list_2)
'''

### 리스트 초기화 ###
a = [1, 2 ,3, 4, 5]
print(a)
print(a[0])   #인덱스 참조

# for문을 이용한 참조
for i in range(5):
    print(a[i], end=' ')
print()
for e in a:
    print(e, end=' ')
print()

# range 함수를 이용한 리스트 초기화
b = list(range(1, 11))
print(b)

# 리스트 append시키기.
c = a + b
d = b + a
print(c)
print(d)