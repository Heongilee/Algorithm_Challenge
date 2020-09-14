def sol(N):
    if(N == 1):
        print(1, end='')
        return
    sol(N // 2)
    print(N % 2, end='')
    return 
    
if __name__ == "__main__":
    N = int(input())
    sol(N)