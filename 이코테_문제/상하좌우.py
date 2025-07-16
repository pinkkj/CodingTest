N = int(input())
direct = list(map(str, input().split()))
a = 1
b = 1
for d in direct:
    if d == "R":
        b = b + 1
        if (b > N):
            b = b - 1
    elif d == "L":
        b = b - 1
        if (b < 1):
            b = b + 1
    elif d == "U":
        a = a - 1
        if (a < 1):
            a = a + 1
    else:
        a = a + 1
        if (a > N):
            a = a - 1

print(a,b)

# 시뮬레이션 유형