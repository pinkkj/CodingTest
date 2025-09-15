N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
A.sort()
B = list(map(int, input().split(' ')))
for i in range(K-1,-1,-1):
    max_num_in_B = max(B)
    if A[i] < max_num_in_B:
        A[i], B[B.index(max_num_in_B)] = B[B.index(max_num_in_B)], A[i]
print(A)
print(B)
print(sum(A))