import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    vowels = ['a', 'e', 'i', 'o', 'u']
    for line in sys.stdin:
        esc = False
        text = line.rstrip()
        if text == 'end':
            break

        if all (t not in vowels for t in text):
            print("<" + text + "> is not acceptable.")
            continue

        if len(text) >= 3:
            f = None   # True면 자음(Consonants) False면 모음(Vowels)
            cnt = 0    # cnt가 3이 되는 순간 out
            for i in range(len(text)):
                if text[i] in vowels:
                    if not f:   # 모음 -> 모음
                        cnt += 1
                        if cnt >= 3:
                            esc = True
                            print("<" + text + "> is not acceptable.")
                            break
                    else:       # 자음 -> 모음
                        f = False
                        cnt = 1
                else:
                    if f:       # 자음 -> 자음
                        cnt += 1
                        if cnt >= 3:
                            esc = True
                            print("<" + text + "> is not acceptable.")
                            break
                    else:       # 모음 -> 자음
                        f = True
                        cnt = 1
            if esc: continue
        
        for i in range(1, len(text)):
            if text[i] == text[i - 1] and (text[i] != 'e' and text[i] != 'o'):
                esc = True
                print("<" + text + "> is not acceptable.")
                break
        if esc: continue
        print("<" + text + "> is acceptable.")

        

