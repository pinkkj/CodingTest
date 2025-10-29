from collections import deque

n = int(input()) 
graph = [[] for _ in range(n+1)]
insert = [0] * (n+1)
times = [[0,[]] for _ in range(n+1)]
for i in range(1,n+1):
    num = 0 
    info = input()
    for k in info.split():
        if int(k) != -1:
            if (num != 0):
                graph[int(k)].append(i)
                insert[i] += 1
            else:
                times[i][0] += int(k)
            num += 1
q = deque()
for i in range(1, n+1):
    if insert[i] == 0:
        q.append(i)


while q:
    now = q.popleft()
    if graph[now]:
        for i in graph[now]:
            insert[i] -= 1
            times[i][1].append(times[now][0])
            if insert[i] == 0:
                q.append(i)
                add_time = max(times[i][1])
                times[i][0] += add_time

for i in range(1, n+1):
    print(times[i][0])

