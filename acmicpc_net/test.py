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
#################################################################
# *, ** means
############################################################
def f2(**kwargs):
    print(kwargs, type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())

    for K, V in kwargs.items():
        print("Key :", K, ", Value :", V)

f2(K1 = "V1", K2 = "V2", K3 = "V3", K4 = "V4")