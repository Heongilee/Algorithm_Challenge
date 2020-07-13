import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
###############################################
'''
# in : 
20
13 34 17 6 11 15 27 42 39 31 25 36 32 25 17 45 67 89 24 65


# out : 
33 2
'''

##############################################
N = int(input())
s = list(map(int, input().split()))

avg = round(sum(s) / N)

min = 2147000000
score = 0
res = 0
for idx, elem in enumerate(s):
    tmp = abs(avg - elem)
    if(tmp < min):
        min = tmp
        score = elem
        res = idx + 1
    elif(min == tmp and elem > score):
        score = elem
        res = idx + 1

print(avg, res, sep=' ')
#########################################################
'''
## map() 함수 문법 참고 ##

# 문법
map(function, iterable)

-> iterable의 각 요소가 함수에 의해 수행된 결과를 묶어서 map iterable 객체로 묶어서 리턴함.

## round() 함수의 반올림 방식의 문제점 ##
Python의 round함수는 round_half_even 방식을 택한다.(실수 값이 정확히 절반 지점에 있다면, 짝수쪽으로 반올림 해버림.)

Ex) 4.50000 의 반올림(round_half_even)은 4가 됨.    -> 5가 되어야 하는데 4가 됨.
Ex) 4.50001 의 반올림(round_half_even)은 5가 됨.
Ex) 5.50000 의 반올림(round_half_even)은 6가 됨.
'''