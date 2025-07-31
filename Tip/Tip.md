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

# ord 함수
- ord()는 문자를 해당 유니코드(ASCII) 정수로 변환해주는 파이썬 내장 함수입니다.
- 보통 알파벳을 숫자로 바꾸기 위해 이용합니다.

```py
col = ord(position[0]) - ord('a') + 1
```

# 이동 문제 풀때의 Tip
- dx와 dy를 (a,b)로 나타내고, steps = [(),()]와 같이 나타낸다.
- dx, dy라는 별도의 리스트를 만들어 관리한다.

# 리스트 컴프리 헨션
- 2차원 리스트 선언 시 효율적
```py
d = [[0]*m for _ in range(n)]
```

# global 변수
- 함수 바깥에서 선언된 전역변수를 이용해야하기 때문.

# 리스트 -> str
```py
arr = ['가', '나', '다', '라', "BlockDMask", '마']
print(arr)

# 그냥 하나의 문자열로 합쳐버리기
str = ''.join(arr)
print(str)
``