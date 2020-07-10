'''
### upper / lower 함수 : 문자열을 전부 대문자 / 소문자화 시킨다. ###
msg = "It is Time"
print(msg.upper())  #모든 문자열을 다 대문자화 시켜 출력함.
print(msg.lower())  #모든 문자열을 다 소문자화 시켜 출력함.

### find 함수 : 해당 문자가 발견된 최초 인덱스를 반환함. ###
print("T의 인덱스는", msg.find('T'))
print("T의 인덱스는", msg.upper().find('T'))

### count 함수 : 해당 문자가 문자열에 몇 개 포함되어 있는지 출력함. ###
print("T의 개수는 :", msg.count('T'))
print("T의 개수는 :", msg.upper().count('T'))

### slice 하기. ###
msg = "It_is_Time"
print(msg)
print(msg[:3])      # 0 ~ 2번 인덱스까지 문자열 추출하는 기능.
print(msg[3:6])     # 3 ~ 5번 인덱스에 해당하는 문자열 추출.
print(msg[6:10])    # 6 ~ 9번 인덱스에 해당하는 문자열 추출.
### 문자열 길이 구하기 (len([문자열])) ###
msg = "It_is_Time"
print(len(msg))

print("[1] : ", end='')
for i in range(len(msg)):
    print(msg[i], end=' ')
print()
print("[2] : ", end='')
for c in msg:
    print(c, end=' ')

### 대문자냐? / 소문자냐? ###
msg = "It_is_Time"
for c in msg:
    if(c.isupper()):
        print("U", end='')
    elif(c.islower()):
        print("L", end='')
    else:
        print("_", end='')
print()

msg = "It is Time"
for c in msg:
    if(c.isalpha()):
        print(c, sep='', end='')
    else:
        continue
tmp = 'AZ'
for x in tmp:
    print(ord(x), end=' ')  #아스키 코드값을 출력하는 함수.
print()  

A = 65
print(A, "의 아스키 코드는 ", chr(A), "입니다.")
'''