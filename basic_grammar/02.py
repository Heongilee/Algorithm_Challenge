'''
'''
# input single value
a = input("숫자 입력 : ")
print(a)

# input multiple value
a, b = input("숫자 입력 : ").split()
print(a, b, sep=', ')   # 2, 3
print(type(a))  # <class 'str'>
print(a + b)    # 23

# 숫자 입력을 받아 연산을 하려면 어떻게 해야 할까?
a, b = map(int, input("숫자를 입력 : ").split())    # 2 3
print(a + b)   # 5
print(a - b)   # -1
print(a * b)   # 6
print(a / b)   # 0.6666666...
print(a // b)   # 0 (몫을 구하는 것)
print(a % b)   # 2 (modulo)
print(a**b) #2^3 (2를 3번 곱한 것.)