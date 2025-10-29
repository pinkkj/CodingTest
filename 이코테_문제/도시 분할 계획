n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

cost_ist = []
city = set()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        cost_ist.append(cost)
        city.add(a)
        city.add(b)

if len(city) == n:
    cost_ist.sort()
    cost_ist.pop()

print(sum(cost_ist))