N, M = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
parent = [0] * (N + 1)
for i in range(1, N+1):
    parent[i] = i
result=[]
for _ in range(M):
    mode, a, b = map(int, input().split())
    if mode == 0:
        union(parent, a, b)
    elif mode == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)

# 주의: N과 M의 범위가 모두 최대 100,000 이므로 경로 압축 방식