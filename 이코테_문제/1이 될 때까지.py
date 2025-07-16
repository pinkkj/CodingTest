N, K = map(int, input().split())
result = 0
while (N != 1):
    if ((N % K) != 0):
        N = N - 1
        result = result + 1
    else:
        N = N // K
        result = result + 1

print(result)
# O(log N)