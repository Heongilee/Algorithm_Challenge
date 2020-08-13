N = int(input())
meeting = []

for _ in range(N):
    s, e = map(int, input().split())
    meeting.append((s, e))

# TIP : 튜플에서 앞에 자료 값을 기준으로 정렬을 수행한다.
# meeting.sort()

# 튜플 리스트에서 뒤의 값 자료를 기준으로 정렬하려면 다음과 같이 쓴다. (key 이용.)
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 0
et = 0
for s, e in meeting:
    if(s >= et):
        et = e
        cnt += 1
        
print(cnt)