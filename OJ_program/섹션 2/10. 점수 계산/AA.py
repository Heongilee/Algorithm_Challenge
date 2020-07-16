f = False
N = int(input())

def swap_f(f):
    return False if (f == True) else True

grading_cnt = 1
score = 0
for a in map(int, input().split()):
    if(a == 0):
        if(f == 1):
            f = swap_f(f)
        grading_cnt = 1
    else:
        if(f == 0):
            f = swap_f(f)
        else:
            grading_cnt += 1
        
        score += grading_cnt
        
print(score)