# DEC to BIN
res = bin(13)
print(res, type(res))  # 0b1101 <class 'str'>

# BIN to DEC
res = int('0b1101', 2)
print(res, type(res))   # 13 <class 'int'>

# and
# 두 숫자가 모두 1일때만 1을 반환
res = int('0b1101', 2) & int('0b1001', 2)
print(bin(res))

# or
# 두 숫자중 하나라도 1이면 1을 반환
res = int('0b1101', 2) | int('0b1001', 2)
print(bin(res))

# xor
# 두 숫자가 서로 다를때 1을 반환
res = int('0b1101', 2) ^ int('0b1001', 2)
print(bin(res))


# not
# 1->0 , 0->1
res = ~int('0b1101', 2)
print(bin(res))


# right-shift
# shiftCnt = 2
# '0b1100'(12) >> shiftCnt == '0b0011'(3)
# 12 * (1 // 2 ** shiftCnt) == 3
res = int('0b10000000', 2)
print("res is " + str(res))
for shiftCnt in range(1, 6):
    print("res >> "+ str(shiftCnt) +" is  " + str(res >> shiftCnt))

# left-shift
# shiftCnt = 2
# '0b0011'(3) >> shiftCnt == '0b1100'(12)
# 3 * (2 ** shiftCnt) == 12
res = int('0b00000001', 2)
print("res is " + str(res))
for shiftCnt in range(1, 9):
    print("res << "+ str(shiftCnt) +" is  " + str(res << shiftCnt))
