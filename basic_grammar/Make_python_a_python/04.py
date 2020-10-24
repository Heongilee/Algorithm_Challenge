'''
s, n = input().strip().split(' ')
n = int(n)

# 우측 정렬의 예시
answer = ''
for i in range(n - len(s)):
    answer += ' '
answer += s
print(answer)
'''
###########################################################
s = '가나다라'
n = 7

print(s.ljust(n))   # 좌측 정렬
print(s.center(n))  # 가운데 정렬
print(s.rjust(n))   # 우측 정렬