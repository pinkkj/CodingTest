N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

each_small_number = []
for i in range(N):
    each_small_number.append(min(array[i]))

result = max(each_small_number)
print(result)