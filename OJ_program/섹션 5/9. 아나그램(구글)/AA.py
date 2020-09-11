A = input()
B = input()
H = dict()

# A에는 있고 B에는 없는 문자의 경우, 1
# A와 B 둘다 있는 문자의 경우, 0
# A에는 없고 B에는 있는 문자의 경우, -1
for x in A:
    H[x] = H.get(x, 0) + 1
for x in B:
    H[x] = H.get(x, 0) - 1

if any (H.get(x) != 0 for x in H.keys()):
    print("NO")
else:
    print("YES")
