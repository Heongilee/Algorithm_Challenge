'''
num = int(input().strip())

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet if (num == 0) else alphabet.upper())
'''
###########################################################
import string

print(string.ascii_lowercase)   # 소문자
print(string.ascii_uppercase)   # 대문자
print(string.ascii_letters)     # 소문자, 대문자 순.
print(string.digits)            # 0 부터 9 까지
