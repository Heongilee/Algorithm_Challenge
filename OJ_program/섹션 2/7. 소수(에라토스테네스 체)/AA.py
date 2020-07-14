########################## 에라토스테네스의 체 #####################################
# prime_number_list = []
def Tot_Prime(e):
    tot = 0
    cnt = [0] * (e + 1)
    for i in range(2, e + 1):
        if(cnt[i] == 0):
            # prime_number_list.append(i)
            tot += 1
            for j in range(i, e + 1, i):
                cnt[j] += 1
    return tot

N = int(input())

print(Tot_Prime(N))
# print(prime_number_list)