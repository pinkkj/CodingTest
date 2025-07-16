# 입력
### 함수
- map(int, input().split())<br><br>
- map(int, input().split())는 map 객체를 반환
- 그 자체로 출력하면 주소 형태가 출력됨 (<map object at ...>)
- list()나 tuple()로 감싸서 실질적인 값을 확인하거나 변수로 언팩해서 사용해야 함.

# 상하좌우 문제 TIP
```py
for d in direct:
    if d == "R":
        b = b + 1
        if (b > N):
            b = b - 1
    elif d == "L":
        b = b - 1
        if (b < 1):
            b = b + 1
    elif d == "U":
        a = a - 1
        if (a < 1):
            a = a + 1
    else:
        a = a + 1
        if (a > N):
            a = a - 1
```
이걸
```py
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny
```
