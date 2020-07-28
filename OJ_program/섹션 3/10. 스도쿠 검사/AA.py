N = 9

def check(a):
    for i in range(N):
        ch1 = [0] * 10  # 0번 인덱스를 제외한 1~9번 인덱스를 사용해 check!
        ch2 = [0] * 10  # 0번 인덱스를 제외한 1~9번 인덱스를 사용해 check!
        for j in range(N):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if( sum(ch1) != N or sum(ch2) != N):
            return False
    
    d = 3
    for i in range(d):
        for j in range(d):
            ch3 = [0] * 10  # 0번 인덱스를 제외한 1~9번 인덱스를 사용해 check!
            for k in range(d):
                for l in range(d):
                    ch3[a[i * d + k][j * d + l]] = 1
            if(sum(ch3) != N):
                return False    
    return True

# Main
a = [list(map(int, input().split())) for _ in range(N)]

if check(a):
    print("YES")
else:
    print("NO")
