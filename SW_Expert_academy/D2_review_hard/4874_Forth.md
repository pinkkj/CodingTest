# 내 코드
```py
T = int(input())
for tc in range(1, T+1):
    stack = []
    result = 'error'
    vals = list(input().split())
    for i, info in enumerate(vals):
        if info.isnumeric():
            stack.append(info)
        elif info == '.':
            try:
                val = stack.pop()
            except:
                result = 'error'

            if stack or (i != (len(vals)-1)):
                result = 'error'
                break
            else:
                result = val
        else:
            try:
                b = int(stack.pop())
                a = int(stack.pop())
            except:
                result = 'error'
                break
            if info == "+":
                stack.append(a+b)
            elif info == "-":
                stack.append(a-b)
            elif info == "*":
                stack.append(a*b)
            elif info == "/":
                stack.append(a/b)
    print(f"#{tc} {result}")
```
=> 10/7 ...(앗, 나눗셈을 /로 해서 float로 나온게 원인..)
# GPT 피드백
## 고칠점
### . 처리 부분에서 런타임 에러 가능성 있음
```py
elif info == '.':
    try:
        val = stack.pop()
    except:
        result = 'error'

    if stack or (i != (len(vals)-1)):
        result = 'error'
        break
    else:
        result = val
```
문제점:
1. 스택이 비어있어서 stack.pop()에서 예외가 나면
    - except:에서 result = 'error'만 하고 끝
    - 그 뒤에 바로 if stack or ... / else: result = val이 실행됨
    - 근데 이때 val은 정의되지 않은 변수 → UnboundLocalError 런타임 에러

## 정리한 버전
```py
T = int(input())
for tc in range(1, T+1):
    stack = []
    result = 'error'
    vals = input().split()

    for i, info in enumerate(vals):
        if info.isnumeric():
            stack.append(int(info))
        elif info == '.':
            # '.'은 마지막 토큰이어야 하고, 스택에 값이 정확히 하나만 있어야 함
            if len(stack) != 1 or i != len(vals) - 1:
                result = 'error'
            else:
                result = stack.pop()
            break
        else:
            # 연산자 처리
            if len(stack) < 2:
                result = 'error'
                break

            b = stack.pop()
            a = stack.pop()

            if info == "+":
                stack.append(a + b)
            elif info == "-":
                stack.append(a - b)
            elif info == "*":
                stack.append(a * b)
            elif info == "/":
                stack.append(a // b)  # 정수 나눗셈
            else:
                # 정의되지 않은 연산자
                result = 'error'
                break

    print(f"#{tc} {result}")
```