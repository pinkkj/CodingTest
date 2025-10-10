# 회사: 1 ~ N번까지의 회사 -> 특정 회사는 도로로 연결(1만큼의 시간 걸림.)
# A는 1번 회사! K번 회사 -> X번 회사. 
N, M = map(int, input().split(" "))
INF = int(1e9)
distance = [[INF] * (N+1) for _ in range(N+1)]
answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            distance[i][j] = 0
for _ in range(M):
    a, b = map(int, input().split(" "))
    distance[a][b] = 1
    distance[b][a] = 1

X, K = map(int, input().split(" "))
# # 확인
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         print(distance[i][j], end=" ")
#     print()
# 알고리즘 시작
for now in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            distance[start][end] = min(distance[start][end], distance[start][now] + distance[now][end])

if distance[1][K] != INF:
    answer += distance[1][K]
    if distance[K][X] != INF:
        answer += distance[K][X]
        print(answer)
    else:
        print(-1)
else:
    print(-1)