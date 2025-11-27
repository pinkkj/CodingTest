# 파이썬에서 EOF까지 입력 받는 법
## 방법 1: sys.stdin으로 한 줄씩 돌기 (제일 깔끔)
```py
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:    # 공백 줄 방지용 (굳이 없어도 되는 경우 많음)
        continue
    s, t = line.split()
    # 여기서 s와 t로 문제 로직 처리
```
- for line in sys.stdin: 은
입력이 끝날 때까지 자동으로 한 줄씩 읽다가, EOF에서 알아서 종료해 줘.

## 방법 2: while True + input() + EOFError 처리
```py
while True:
    try:
        s, t = input().split()
    except EOFError:
        break
    
    # 여기서 s와 t로 문제 로직 처리
```
- 더 이상 입력이 없으면 input()이 EOFError를 던짐
- 그때 break로 빠져나오는 방식