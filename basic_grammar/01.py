# 메모리가 사용 가능한 숫자 자리수에 제한 없이 출력 가능함.
a = 1
b = 2
c = 3

# 소수부가 0일때, 0을 생략
d = 5.
print(d)

# 정수부가 0일때, 0을 생략
e = -.7
print(e)

# [유효숫자]e[지수] 형태로 수 표현이 가능.
f = 1e9
print(f)

# round(실수, 소숫점 아래 몇번째 자리까지?) 함수로 
# round(g, 2) == 3752.34 가 되는 이유(원래는 3752.35로 올림 처리)는 Python에서 반올림을 Round_half_even 방식을 사용하기 때문이다.
g = 3.7523450e3
print("g : ", g, ", roung(g, 2)", round(g, 2))

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