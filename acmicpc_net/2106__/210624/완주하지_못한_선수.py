from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(list)
    for p in participant: dic[p].append([len(dic[p]), False])
    for c in completion:
        for i in range(len(dic[c])):
            if not dic[c][i][1]:
                dic[c][i][1] = True
                break
    for K, V in dic.items():
        for i in range(len(V)):
            if not V[i][1]: return K
        

if __name__ == '__main__':
    res = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    # res = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    # res = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
    print(res)