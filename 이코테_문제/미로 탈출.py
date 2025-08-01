# 내 풀이
N, M = map(int, input().split(' '))
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

step = 0
def dfs(graph, x, y):
    global step
    if not(x <= -1 or x >= N or y <= -1 or y >= M):
        if graph[x][y] == 1:
            step = step + 1
            graph[x][y] = 0
            if (x==(N-1) and y == (M-1)):
                return True

            up = dfs(graph, x-1,y) #False # False
            down = dfs(graph, x+1,y)
            right = dfs(graph, x, y+1)

            if not (up or down or right):
                step = step - 1
                return False
            
            return True
        else:
            return False
    else:
        return False



dfs(graph, 0, 0)
print(step)

# 책 풀이 (BFS 이용)
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))

# 📌 정리
# 상하좌우만 이동할 수 있는 단순한 빈 격자라면 최단 거리는 항상 같음.
# → 하지만 미로 문제는 벽(0)이 있으므로, 실제 최단 거리는 DFS로 바로 알 수 없음.

# BFS는 가까운 거리부터 탐색하므로 벽을 고려한 최단 거리를 보장할 수 있어.