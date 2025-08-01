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
```

# 시간 복잡도
### ✅ 코딩테스트에서 생각할 기준
- 문제의 n 크기 확인

n ≤ 10³ → O(n²)도 가능

n ≤ 10⁵ → O(n log n)까지만 안전

n ≥ 10⁶ → O(n) 또는 O(log n)만 가능

- 제한 시간 확인 (대부분 1~2초)

- 1초 안에 약 1억 번 연산까지 가능 (파이썬은 5천만 번 정도로 잡는 게 안전)

- O(n²) 이하라도, 내부에서 슬라이싱·pop(0) 같은 O(n) 연산이 섞이면 사실상 O(n³) 비슷해질 수 있음

### 🔑 결론
- n이 10만 이상이면 무조건 O(n log n) 이하로 설계해야 안전합니다.
- "O(n²) 이하니까 괜찮다" → X (입력 크기에 따라 달라짐)

- 문제에서 입력 크기를 먼저 보고 시간 복잡도 목표를 세워야 합니다.
- 파이썬에서 1초에 약 5천만 연산 정도 가능
- 코딩테스트에서 O(n²) 는 n이 2000~3000 정도일 때만 괜찮음