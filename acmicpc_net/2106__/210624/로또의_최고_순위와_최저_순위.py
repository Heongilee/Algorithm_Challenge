ranks = [-1, 6, 5, 4, 3, 2]
def ranking(cnt):
    for i in range(1, 6):
        if cnt >= ranks[i]: return i
    else:
        return 6

def solution(lottos, win_nums):
    res = []
    dic = dict(zip(win_nums, [0] * 6))
    lottos = sorted(lottos, reverse=True)
    i = 0
    while i < 6 and lottos[i] > 0:
        if dic.get(lottos[i], None) != None: dic[lottos[i]] += 1
        i += 1

    cnt = 0
    for _, V in dic.items():
        if V >= 1: cnt += 1
    res.append(ranking(cnt))

    cnt += (6 - i) if abs(6 - cnt) >= 6 - i else abs(6 - cnt)
    res.append(ranking(cnt))

    res.reverse()
    return res

if __name__ == '__main__':
    # res = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])   #[3, 5]
    # res = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])  #[1, 6]
    res = solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])  #[1, 1]
    print(res)
    