import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

# Euclidean algorithm : A와 B의 최대공약수는 B과 R(A를 B로 나눈 나머지)의 최대공약수와 같다.
def gcd(A, B):
    return B if(A % B == 0) else gcd(B, A%B)

def lcm(A, B):
    return (A*B) / gcd(A, B)
if __name__ == "__main__":
    print(gcd(192, 162))
    print(lcm(192, 162))