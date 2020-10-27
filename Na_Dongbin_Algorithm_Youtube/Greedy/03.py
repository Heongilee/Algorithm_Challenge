import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

'''
if __name__ == "__main__":
    a = list(map(int, input()))
    
    res = a[0]
    for i in range(1, len(a)):
        if(res + a[i] > res * a[i]):
            res += a[i]
        else:
            res *= a[i]
    print(res)
'''
###############################################################################
if __name__ == "__main__":
    a = list(map(int, input()))
    
    result = a[0]
    for i in range(1, len(a)):
        num = a[i]
        
        if(num <= 1 or result <= 1):
            result += num
        else:
            result *= num
    print(result)