N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
large_num = numbers[N-1]
second_large_num = numbers[N-2]

large_num_sum = M // K
second_sum = M % K

result = large_num * K *large_num_sum + second_large_num * second_sum
print(result)