N = int(input())
for i in range(N):
    s = input()
    s = s.upper()
    rs = s[::-1]    # array slice & reverse!
    if(s == rs):
        print("#%d YES" %(i + 1))
    else:
        print("#%d NO" %(i + 1))