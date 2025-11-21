# 내 코드
```py
for stage in range(1, 11):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for j in range(100):
        pre = (-1, 0)
        for i in range(100):
            if (pre == (-1, 0)) and (info[i][j] == 2):
                continue
            elif (pre == (-1, 0)) and (info[i][j] == 1):
                pre = (1, i)
            elif (pre[0] == 1) and (info[i][j] == 2):
                result += 1
                pre = (-1, 0)
    print(f"#{stage} {result}")
```
# GPT 피드백
## 더 단순화
```py
for stage in range(1, 11):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for j in range(N):
        has_N = False
        for i in range(N):
            if info[i][j] == 1:
                has_N = True            # 위에서 1 등장
            elif info[i][j] == 2 and has_N:
                result += 1             # 1 밑에 2 → 교착
                has_N = False           # 다시 초기화

    print(f"#{stage} {result}")
```
- 0은 그냥 아무 조건도 안 걸려서 자동 무시
- 2도 has_N 없으면 아무 일도 안 함