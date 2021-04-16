import sys, itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
############################################################################
# Sol - 비트 마스킹 연산
#######################################################################
def word_to_binary(word):
    res = 0b0
    for w in word:
        res = res | (1 << alpha_code[w])

    return res

if __name__ == '__main__':
    # k - 5개의 알파벳에 대해 코드를 부여
    # 해당 값은 비트 1을 오른쪽부터 shift한 횟수를 의미하기도 함.
    
    n, k = map(int ,input().split())

    if k < 5:
        print(0)
        sys.exit(0)

    alpha_code = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}
    words = [set(input().rstrip()[4:-4]).difference('a', 'c', 'i', 'n', 't') for _ in range(n)]
    binaries = [word_to_binary(word) for word in words]
    power_of_2 = [2 ** i for i in range(21)]
    maxcnt = None

    for X in it.combinations(power_of_2, k - 5):
        cnt = 0
        for binary in binaries:
            if binary & sum(X) == binary:
                cnt += 1
        
        maxcnt = max(maxcnt, cnt) if maxcnt else cnt

    print(maxcnt)

############################################################################
# Sol - 백트래킹으로 풀기 (Pypy3 메모리 초과, Python3 시간 초과)
#######################################################################
'''
sys.setrecursionlimit(10 ** 6)
def DFS(L, S):
    global ans

    if L == k - 5:
        cnt = 0
        for word in words:
            for w in word:
                if not alphaLearning[ord(w) - ord('a')]:
                    break
            else:
                cnt += 1
        ans = max(ans, cnt) if ans else cnt
        return 

    else:
        for i in range(S, 26):
            if not alphaLearning[i]:
                alphaLearning[i] = True
                DFS(L + 1, i)
                alphaLearning[i] = False
    
if __name__ == '__main__':
    ans = None
    n, k = map(int, input().split())

    if k < 5 or k == 26:
        print(0 if k < 5 else n)
        sys.exit(0)
        
    words = [input().rstrip() for _ in range(n)]
    alphaLearning = [False] * 26
    # prefix = anta, suffix = tica는 fix
    # k가 5 이상일 경우, {a, n, t, i, c}를 제외한 k - 5개의 글자로 
    # 최대한 많은 단어를 학습할 수 있는 경우의 수를 구함.
    for c in ('a', 'n', 't', 'i', 'c'):
        alphaLearning[ord(c) - ord('a')] = True

    S = set(string.ascii_lowercase).difference(set(['a', 'n', 't', 'i', 'c']))
    for X in it.combinations(S, k - 5):
        cnt = 0
        for word in words:
            if len(word) <= 8:
                cnt += 1
                break
            else:
                word = word[4:len(word) - 4]
                for w in word:
                    if w not in X:
                        break
                else:
                    cnt += 1
        ans = max(ans, cnt) if ans else cnt
    print(ans)
'''
    

############################################################################
# my answer (0% WA)
#######################################################################
'''
if __name__ == '__main__':
    n, k = map(int, input().split())    # 1 <= n <= 50, 0 <= k <= 26
    dic = [input().rstrip() for _ in range(n)]

    res = list(''.join(dic))
    res = sorted(res, key=lambda x:-res.count(x))
    res = deque(res)

    S = set()
    while res and len(S) < k:
        S.add(res.popleft())
    
    if not res:
        # 집합에 k개만큼 채워넣기전에 res가 다 닳았다는 것은
        # k개 글자 미만으로 n개의 단어를 모두 학습할 수 있다는 것으로
        # 답은 n개 모두가 정답이다.
        print(n)
    else:
        cnt = 0
        for d in dic:   # word in dictionary
            d = set(d)
            for c in d: # character
                if c not in S:
                    break
            else:
                cnt += 1
        print(cnt)
'''

############################################################################
# 테스트 코드
#######################################################################
'''
import heapq as hq
if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [input().rstrip() for _ in range(n)]
    dic = dict()

    for word in arr:
        for c in word:
            dic[c] = dic.get(c, 0) + 1
    
    pq = []
    for K, V in dic.items():
        hq.heappush(pq, (-V, K))
    
    cnt = 0
    while cnt < k:
        a, b = hq.heappop(pq)
        a *= -1
        print(a, b)
        cnt += 1
'''