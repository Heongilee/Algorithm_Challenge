import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

if __name__ == '__main__':
    N = 4
    a = list(int(input()) for _ in range(N))
    
    balance = 1260
    count = 0
    
    for i in a:
        count += balance // i
        balance %= i
    print(count)
    
    