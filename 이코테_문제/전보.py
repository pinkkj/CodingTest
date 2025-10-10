# N개의 도시
# 양방향X 단방향!
# 목표: C라는 도시에서 최대한 많은 도시로 메시지 보내!!
# 시간복잡도 때문에 다이스트라 쓰는게 좋을듯.
import sys
import heapq
input = sys.stdin.readline
N, M, C = map(int, input().split(" "))
INF = int(1e9)
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, Z = map(int, input().split(" ")) # X: 출발 / y: 도착 / z: 시간
    graph[X].append((Z,Y))

q = []

def dij():
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            for info in graph[now]:
                cost = dist + info[0]
                if cost < distance[info[1]]:
                    distance[info[1]] = cost
                    heapq.heappush(q, (cost, info[1]))
        else:
            continue

heapq.heappush(q, (0,C))
dij()

num = 0
time = 0
for dist in distance:
    if dist != INF:
        num += 1
        if time < dist:
            time = dist
print(num, time)

# 책 ver
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split(" "))
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    X, Y, Z = map(int, input().split(" ")) # X: 출발 / y: 도착 / z: 시간
    graph[X].append((Z,Y))



def dij(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0 # 빠트림.
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            for info in graph[now]:
                cost = dist + info[0]
                if cost < distance[info[1]]:
                    distance[info[1]] = cost
                    heapq.heappush(q, (cost, info[1]))
        else:
            continue


dij(C)

num = 0
time = 0
for dist in distance:
    if dist != INF:
        num += 1
        if time < dist:
            time = dist
print(num-1, time)