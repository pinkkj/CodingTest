# 내 코드
```py
T = int(input())
for stage in range(1, T+1):
    global N, result
    N = int(input())
    result = 0
    visited = [False] * (N+1)
    diag = [False] * 2 * N
    right_diag = [False] * 2 * N
    def dfs(row):
        global N, result
        if row == N:
            result += 1
            return
        for col in range(N):
            if visited[col] or diag[row+col] or right_diag[row-col+N-1]:
                continue
            visited[col] = True
            diag[row+col] = True
            right_diag[row-col+N-1] = True
            dfs(row+1)
            visited[col] = False
            diag[row+col] = False
            right_diag[row-col+N-1] = False
    dfs(0)
    print(f"#{stage} {result}")
```
# GPT 피드백
## 배열 크기 & 표현 자잘한 개선
- col은 0 ~ N-1만 쓰니까, 사실 N+1까지 필요 없어 .정확히 필요한 만큼만 잡는 게 조금 더 깔끔해:
```py
visited = [False] * N
```