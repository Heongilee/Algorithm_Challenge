'''
함수 만들기

# C언어처럼 전처리자가 없기 때문에 항상 함수 정의부는 위에 배치 시킬 것.
def add(a, b):
    c = a + b
    print(c)

add(3, 2)
######################################################################################
# 튜플 형태로 리턴하는 함수.
def calc(a, b):
    c = a + b
    d = a - b
    return c, d

a, s = calc(3, 2)
print(a, ",", s)

'''
def isPrime_1(x):
    if any((x%i == 0) for i in range(2, x)):
        return False
    else:
        return True

def isPrime_2(x):
    for i in range(2, x):
        if(x%i == 0):
            return False
    else:
        return True
######################################################################################
a = [12, 13, 7, 9, 19]
for y in a:
    if(isPrime_1(y)):
        print(y, end=' ')