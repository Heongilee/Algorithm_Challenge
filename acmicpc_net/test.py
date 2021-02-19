nums = ["8", "2", "3"]
N = "5457"

if all (n not in N for n in nums):
    print("YES")
else:
    print("NO")