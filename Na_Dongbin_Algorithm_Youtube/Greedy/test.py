import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt")

if __name__ == "__main__":
    n = int(input())
    f = list(map(int, input().split()))
    g = 0
        
    f.sort(reverse=True)

    i=0
    while(i < n):
        if(i + f[i] <= n):
            g += 1
            i += f[i]
    print(g)