import sys

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