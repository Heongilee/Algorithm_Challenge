import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

if __name__ == '__main__':
    time = [0, 0, 0]
    
    N = int(input())
    count = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)
            