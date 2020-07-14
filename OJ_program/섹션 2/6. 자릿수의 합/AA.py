N = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    # x 정수값을 string으로 타입 캐스팅해서 문자 하나하나를 처리함. -> Python이니까 가능한 것.
    for i in str(x):
        sum += int(i)
    return sum
        

max_tot = -2147000000
res = a[0]
for x in a:
    tot = digit_sum(x)
    if(tot > max_tot):
        max_tot = tot
        res = x

print(res)