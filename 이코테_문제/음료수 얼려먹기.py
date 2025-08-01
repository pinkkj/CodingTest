N,M = map(int, input().split(' '))
ice_case = []
for i in range(N):
    ice = list(map(int, input()))
    ice_case.append(ice)

#visited = [[False] * M for _ in range(N)]

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if ice_case[x][y] == 0:
        # 해당 노드 방문 처리
        ice_case[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
# 모든 위치에 대해 음료수 채우기
result = 0 
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
print(result)