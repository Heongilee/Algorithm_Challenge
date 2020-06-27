'''
x = 7

# 인덴팅 (띄어쓰기로 4칸)으로 if문 안에 있음을 구분.
if (x == 7):
    print("x는 ", x, end='\t')
    if((x % 2) == 0):
        print("even value")
    else:
        print("odd value")
        
if (x != 7):
    print("x는 ", x, "이 아니다")
    
if(x >= 0 and x <= 10):
    print("0 ≤ x ≤ 10")
'''
x = 82

if (x >= 90):
    print("A")
elif(x >= 80):
    print("B")
elif(x >= 70):
    print("C")
elif(x >= 60):
    print("D")
else:
    print("F")
