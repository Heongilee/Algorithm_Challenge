#################################################################
# Swapping Algorithm without tmp
############################################################
'''
def solution(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    a = 214748
    b = 356419

    print("Before:\t", a, b)
    a, b = solution(a, b)
    print("After:\t", a, b)
'''
from collections import deque
a = "abba"

print(a[:len(a) - 1])