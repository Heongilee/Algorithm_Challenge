# 메모리가 사용 가능한 숫자 자리수에 제한 없이 출력 가능함.
a = 1
b = 2
c = 3

# 콤마로 변수 구분해서 출력.
# print(a, b, c)

# 1, 2, 3
print(a, b, c, sep=', ')

# 1
# 2
# 3
print(a, b, c, sep='\n')

## 기본 \n 을 넣는걸 빼줌.
# 1 2 3
print(a, b, c, end=' ')


# <class 'int'>
print(type(a))