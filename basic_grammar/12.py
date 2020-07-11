'''
람다 함수(Lambda Function)

'''
# 일반적인 함수 사용
def plus_one(x):
    return x + 1

print(plus_one(1))


# 람다 함수 사용
# 변수 = lambda 파라미터: 동작
plus_two = lambda x: x + 2

print(plus_two(1))
# 언제 써? : 내장 함수의 인자로 쓰일 때 유용함.

#람다 함수 안 쓰면 이렇게
a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))



