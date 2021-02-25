import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
a = [list(map(int, input().split())) for _ in range(9)]

# 행 검사
for r in a:
    str_r = str(r)
    for e in range(1, 10):
        str_e = str(e)
        if(str_r.find(str_e) != -1):
           continue
        else:
            print("NO")
            sys.exit()

# 열 검사
for i in range(9):    
    str_r = ""
    for r in a:
        str_r += str(r[i]) + ", "
    for e in range(1, 10):
        str_e = str(e)
        if(str_r.find(str_e) != -1):
            continue
        else:
            print("NO")
            sys.exit()

# 그룹 검사               
dx = [0, 1, 2]
dy = [0, 1, 2]
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        str_r = ""
        for k in range(3):
            for l in range(3):
                str_r += str(a[i + dx[k]][j + dy[l]]) + ", "
        
        for e in range(1, 10):
            str_e = str(e)
            if(str_r.find(str_e) != -1):
                continue
            else:
                print("NO")
                sys.exit()
print("YES")
'''
############################################################################
'''
a = [list(map(int, input().split())) for _ in range(9)]

# 체크리스트 만들어서 관리하기 <- 알아 둘 것
ch1 = [0] * 10  # 행 체크
ch2 = [0] * 10  # 열 체크
ch3 = [0] * 10  # 그룹 체크

# 행 체크
N = 9
for i in range(N):
    ch1 = [0] * 9
    for j in range(N):
        ch1[a[i][j] - 1] = 1
    if(sum(ch1) != N):
        print("NO")
        break

# 열 체크
for i in range(N):
    ch2 = [0] * 9
    for j in range(N):
        ch2[a[j][i] - 1] = 1
    if(sum(ch2) != N):
        print("NO")
        break

d = 3
for i in range(0, N, 3):
    for j in range(0, N, 3):
        ch3 = [0] * 9
        for k in range(i, i + d):
            for l in range(j, j + d):
                ch3[a[k][l] - 1] = 1
        if(sum(ch3) != N):
            print("NO")
            break
else:
    print("YES")
'''
############################################################################
N = 9

def check(a):
    for i in range(N):
        ch1 = [0] * 10  # 0번 인덱스를 제외한 1~9번 인덱스를 사용해 check!
        ch2 = [0] * 10  # 0번 인덱스를 제외한 1~9번 인덱스를 사용해 check!
        for j in range(N):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if( weight(ch1) != N or weight(ch2) != N):
            return False
    
    d = 3
    for i in range(d):
        for j in range(d):
            ch3 = [0] * 10  # 0번 인덱스를 제외한 1~9번 인덱스를 사용해 check!
            for k in range(d):
                for l in range(d):
                    ch3[a[i * d + k][j * d + l]] = 1
            if(weight(ch3) != N):
                return False    
    return True

# Main
a = [list(map(int, input().split())) for _ in range(N)]

if check(a):
    print("YES")
else:
    print("NO")