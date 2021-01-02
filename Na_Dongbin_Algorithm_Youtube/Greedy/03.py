import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt")

if __name__ == "__main__":
    n = list(map(int, input()))
    result = 0

    for i in range(len(n)):
        result = max(result + n[i], result * n[i])
    print(result)
###############################################################################
'''
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
'''