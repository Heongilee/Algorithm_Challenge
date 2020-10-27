import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

if __name__ == '__main__':
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    i = 0
    g = 0
    while(i < len(a)):
        if(i + (a[i] - 1) < len(a)):
            i += (a[i] - 1)
            g += 1
        i += 1
    print(g)