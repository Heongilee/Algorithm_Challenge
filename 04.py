''' 
### range() 함수 ###

a = range(10)

# <class 'range'>
print(type(a))

# <class 'list'>
print(type(list(a)))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(a))

### for문 ###
for i in range(10): # 0 ~ 9 (++i)
    print(i, end=' ')

for i in range(1, 10):  # 1 ~ 9 (++i)
    print(i, end=' ')

for i in range(10, 0, -1):  # 10 ~ 1 (--i)
    print(i, end=' ')
### while문 ###

i = 1
while (i <= 10):    # 1 ~ 10 (++i)
    print(i)
    i += 1

i = 1
while(True):
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    if(i >= 11):
        breㄸak
    i += 1
### for-else구문 ###
# for문 안에서 break문을 만나는 등 정상 흐름이 끊긴다면, else문을 실행하지 않는다.
# 정상 흐름대로 for문이 돌아야 else를 읽는다.
for i in range(1, 11):
    print(i)
    if(i >= 5):
        break
else:
    print("for문이 정상 종료되었습니다.")
'''