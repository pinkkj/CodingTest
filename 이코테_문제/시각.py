N = int(input())
result = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if "3" in time:
                result = result + 1
            
print(result)

# Q. 경우의 수로 풀 수는 없나?
# A. 프로그래밍으로 하는것이 더 쉬움.