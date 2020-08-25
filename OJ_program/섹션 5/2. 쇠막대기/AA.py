a = list(map(str, input()))
S = []

cnt = 0
for i in range(len(a)):
    if(a[i] == '('):
        S.append('(')
    elif(a[i] == ')'):
        S.pop()
        if(a[i - 1] == ')'):
            cnt += 1
        else:
            cnt += len(S)
print(cnt)